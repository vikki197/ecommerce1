import pika


class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare('inventory', exchange_type='topic')

    def publish(self, key, body):
        self.channel.basic_publish(exchange='inventory', routing_key=key, body=body)
        print('message sent')
