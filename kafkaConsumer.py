from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    'cart-events',  # Topic name
    bootstrap_servers='localhost:9092',  # Kafka broker
    auto_offset_reset='earliest',  # Start from the beginning
    enable_auto_commit=True,
    group_id='cart-pyconsumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON
)

print("Listening for cart events...")

for message in consumer:
    print(f"Received: {message.value}")  # Print the JSON message
