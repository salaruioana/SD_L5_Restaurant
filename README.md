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
- Deschide rabbit pe localhost:5672
- creeaza exchange restaurant.direct
- creeaza coada order.queue
- creeaza coada prepared.queue
- adauga binding in exchange: order.queue cu routing key to.kitchen
- adauga binding in exchange: prepared.queue cu routing key to.serve
- Deschide in IntelliJ Cook-Kotlin - pornesti din Kitchen.kt pe verde fun main 
- Deschide in PyCharm Waiter-Python - pornesti din main
