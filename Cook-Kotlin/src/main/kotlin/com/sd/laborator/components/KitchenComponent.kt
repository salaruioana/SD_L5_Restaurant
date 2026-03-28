package com.sd.laborator.components

import com.sd.laborator.interfaces.Cook
import com.sd.laborator.models.Dish
import com.sd.laborator.models.Order
import org.springframework.amqp.core.AmqpTemplate
import org.springframework.amqp.rabbit.annotation.RabbitListener
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Component

@Component
class KitchenComponent {
    @Autowired
    private lateinit var cook: Cook

    @Autowired
    private lateinit var connectionFactory: RabbitMqConnectionFactoryComponent

    // Spring AMQP-Advanced Message Queuing Protocol
    // this class contains methods such as convertAndSend(exchange, routingKey, message) and receiveAndConvert(queueName)
    // that allow us to interact with the messaging queue
    @Autowired
    private lateinit var amqpTemplate: AmqpTemplate

    @RabbitListener(queues = ["\${order.rabbitmq.queue}"], containerFactory = "rabbitListenerContainerFactory")
    fun receieveOrder(order: Order) {
        println(" kitchen > Received order #${order.idOrder} (Menu ${order.typeMenu}) from ${order.idWaiter}")
        val preparedDish = cook.Cook(order)

        println(" kitchen > Order #${order.idOrder} was prepared. Sending dish..")
        sendDish(preparedDish)
        System.out.println("kitchen > Dish sent")
    }

    private fun sendDish(dish: Dish){
        this.amqpTemplate.convertAndSend(
            connectionFactory.getExchange(),
            connectionFactory.getRoutingKey(),
            dish
        )
    }

}