from datetime import datetime
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')


while True:
    msg = input('Enter a message...\n')
    msg = bytes(msg, encoding='utf-8')
    future = producer.send('test_topic', key=b'user1', value=msg)
    result = future.get(timeout=60)
    print(datetime.fromtimestamp(result.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'))
    