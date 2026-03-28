import tkinter as tk
from tkinter import messagebox
import threading
import time
from mq_communication import RabbitMq


class WaiterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Waiter interface- Taking orders")
        self.root.geometry("500x400")

        # initialising RabbitMq communication
        self.rabbitmq = RabbitMq(self)

        # UI Elements
        self.label_title = tk.Label(root, text="Menu options", font=("Arial", 14, "bold"))
        self.label_title.pack(pady=10)

        # 5 buttons for 5 menus
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        for i in range(1, 6):
            btn = tk.Button(self.button_frame, text=f"Menu no {i}",
                            width=20, command=lambda m=i: self.place_order(m))
            btn.pack(pady=2)

        # display
        self.label_status = tk.Label(root, text="Orders status:", font=("Arial", 10, "italic"))
        self.label_status.pack(pady=(20, 0))

        self.text_area = tk.Text(root, height=8, width=55)
        self.text_area.pack(pady=5)

        # Am mutat pornirea thread-ului de ascultare (receive_message) in constructorul __init__.
        # Astfel, cream un SINGUR thread de ascultare "permanent" cand porneste aplicatia.
        # Acest lucru elimina pericolul de a avea zeci de thread-uri care se lupta pe aceeasi coada.
        self.listener_thread = threading.Thread(target=self.rabbitmq.receive_message, daemon=True)
        self.listener_thread.start()

    def place_order(self, menu_type):
        # unique id
        order_id = int(time.time()) % 10000

        self.log_message(f"Sending order #{order_id} (Menu type {menu_type})...")

        # pushing order in mq
        self.rabbitmq.send_order(order_id, menu_type)

    def set_response(self, order_id, message):
        # when the dish is prepared...
        # we use after to update the UI from the main thread
        self.root.after(0, lambda: self.log_message(f"Prepared: #{order_id}: {message}"))

    def log_message(self, msg):
        self.text_area.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {msg}\n")
        self.text_area.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = WaiterApp(root)
    root.mainloop()