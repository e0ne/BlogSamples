from kombu.mixins import ConsumerMixin
from kombu.utils import kwdict, reprcall

from queues import task_queues

class Worker(ConsumerMixin):

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        try:
            return [Consumer(queues=task_queues,
                callbacks=[self.process_task])]
        except Exception, e:
            print e


    def process_task(self, body, message):
        print body['hello']
        message.ack()

if __name__ == "__main__":
    from kombu import BrokerConnection
    from kombu.utils.debug import setup_logging
    setup_logging(loglevel="INFO")

    with BrokerConnection("amqp://guest:guest@192.168.17.25:5672//") as conn:
        try:
            Worker(conn).run()
        except KeyboardInterrupt:
            print("bye bye")