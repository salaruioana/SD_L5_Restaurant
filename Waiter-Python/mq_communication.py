import pika
import json
from retry import retry


class RabbitMq:
    config = {
        'host': 'localhost',
        'port': 5672,
        'username': 'student',
        'password': 'student',
        'exchange': 'restaurant.direct',
        'routing_key': 'to.kitchen',  # waiter sends to kitchen
        'queue': 'prepared.queue'  # waiter brings to table when prepared
    }

    def __init__(self, ui):
        self.ui = ui
        self.credentials = pika.PlainCredentials(self.config['username'], self.config['password'])
        self.parameters = pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port'],
            credentials=self.credentials
        )

    def on_received_message(self, ch, method, properties, body):
        print(f"Received answer from kitchen: {body}")
        try:
            dish_data = json.loads(body.decode('utf-8'))

            id_order = dish_data['idOrder']
            id_cook = dish_data['idCook']
            type_menu = dish_data['typeMenu']

            text = f"Menu {type_menu} is served. (Cooked by: {id_cook})"
            self.ui.set_response(id_order, text)

        except Exception as e:
            print(f"Processing error: {e}")


    def send_order(self, order_id, menu_type):
        order_obj = {
            "idOrder": int(order_id),
            "idWaiter": "Waiter_Python_GUI",
            "typeMenu": int(menu_type)
        }
        json_payload = json.dumps(order_obj)
        self.send_message(json_payload)

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def receive_message(self):
        with pika.BlockingConnection(self.parameters) as connection:
            with connection.channel() as channel:
                channel.queue_declare(queue=self.config['queue'], durable=True)
                channel.basic_consume(queue=self.config['queue'],
                                      on_message_callback=self.on_received_message,
                                      auto_ack=True)
                channel.start_consuming()

    def send_message(self, message):
        with pika.BlockingConnection(self.parameters) as connection:
            with connection.channel() as channel:
                channel.basic_publish(
                    exchange=self.config['exchange'],
                    routing_key=self.config['routing_key'],
                    body=message,
                    properties = pika.BasicProperties(
                        content_type='application/json',
                        delivery_mode=2,  # makes the message persistent
                    )
                )