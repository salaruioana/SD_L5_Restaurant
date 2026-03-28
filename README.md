# Restaurant Order System (Python + Kotlin + RabbitMQ)

A simple project demonstrating bidirectional asynchronous communication between two applications using RabbitMQ.

## Architecture

1. Waiter (Python + Tkinter): A GUI application that sends orders to RabbitMQ and listens for prepared orders in a background thread.
2. Kitchen (Kotlin + Spring Boot): A worker service that consumes orders, simulates cooking, and sends a response back.
3. RabbitMQ: The message broker handling routing and queues.

## Features

- Cross-language messaging using JSON.
- Round-Robin load balancing (supports running multiple Kitchen instances simultaneously).

## Prerequisites

- RabbitMQ running on localhost:5672 (credentials: student / student)
- Python 3.x (required packages: pika, retry)
- Java JDK 17+

## How to Run

1. Start your RabbitMQ server.
2. Run the Python Waiter application:
   python WaiterApp.py
3. Run the Kotlin Kitchen application. 
   Note: You can run multiple instances of the Kotlin app in parallel to test RabbitMQ's load balancing.
