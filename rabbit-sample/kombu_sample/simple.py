import ssl
from kombu import BrokerConnection

#: Create connection
#: If hostname, userid, password and virtual_host is not specified
#: the values below are the default, but listed here so it can
#: be easily changed.

def simple_queue(ca_certs, keyfile, certfile, host, use_ssl=False):

    if use_ssl:
        ssl_opts = {'ca_certs': ca_certs,
                    'keyfile': keyfile,
                    'certfile': certfile,
                    'cert_reqs': ssl.CERT_REQUIRED}
        port = 5671
    else:
        ssl_opts = None
        port = 5672

    with BrokerConnection("amqp://guest:guest@%s:%d//" % (host, port), ssl=ssl_opts) as conn:

        #: SimpleQueue mimics the interface of the Python Queue module.
        #: First argument can either be a queue name or a kombu.Queue object.
        #: If a name, then the queue will be declared with the name as the queue
        #: name, exchange name and routing key.
        with conn.SimpleQueue("kombu_demo") as queue:
            queue.put({"hello": "world"}, serializer="json", compression="zlib")
