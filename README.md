A Simple Python Kafka Consumer.

To create a consumer the python-kafka module has to be installed and used in the project by importing it.
Since JSON data will be read the json module should be imported as well for the proper deserialization of the message like:

from kafka import KafkaConsumer
import json

After that a KafkaConsumer is created like below:

consumer = KafkaConsumer(
    'cart-events',  # Topic name
    bootstrap_servers='localhost:9092',  # Kafka broker
    auto_offset_reset='earliest',  # Start from the beginning
    enable_auto_commit=True,
    group_id='cart-pyconsumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON
)

Messages will be then processed in the following loop

for message in consumer:

The user can process the message and send it to another framework or system like Apache Spark or Flink to be used for analytics purposes
