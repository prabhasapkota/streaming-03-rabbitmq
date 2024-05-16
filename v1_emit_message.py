"""
Author: Prabha Sapkota
Date: 05/16/2024

This program sends a message to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import pika

# Define the message content
message = "This is getting interesting"

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)

# print a message to the console for the user
print(" [x] Sent 'message'")

# close the connection to the server
conn.close()
