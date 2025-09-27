from confluent_kafka import Producer
from config import config

producer = Producer(config)             #Makes Producer ready to be a Producer with needed configurations

def callback(err, event):
    if err:
        print(f'Produce to topic {event.topic()} failed for event: {event.key()}')
    else:
        val = event.value().decode('utf8')          #For string inputs the values are encoded to utf8 format
        print(f'{val} sent to partition {event.partition()}.')

def say_hello(key):
    value = f'Hello {key}!'
    producer.produce('first_topic', value, key, on_delivery=callback)
    producer.flush()          #Makes sure all the messages are sent before moving on
    return value

# if __name__ == '__main__':
    # keys = ['Amy2', 'Brenda2', 'Cindy2', 'Derrick2', 'Elaine2', 'Fred2']
    # keys = ['Bond']
    # [say_hello(producer, key) for key in keys]
    