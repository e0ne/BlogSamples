import ssl
import time
from pika.adapters import SelectConnection
from pika.connection import ConnectionParameters
from pika import BasicProperties
connection = None
channel = None
host = None

def on_connected(connection):
    print "demo_send: Connected to RabbitMQ"

    connection.channel(on_channel_open)


def on_channel_open(channel_):
    global channel
    channel = channel_
    channel.queue_declare(queue="test", durable=True,
        exclusive=False, auto_delete=False,
        callback=on_queue_declared)


def on_queue_declared(frame):
    # Create properties with when we sent the message, the app_id
    # user we connected with, a content type and non persisted messages
    properties = BasicProperties(timestamp=time.time(),
        app_id=__file__,
        user_id='guest',
        content_type="text/plain",
        delivery_mode=1)

    # Send the message
    channel.basic_publish(exchange='',
        routing_key="test",
        body='hello',
        properties=properties)

    # Close our connection
    #connection.close()

def simple_server(ca_certs, keyfile, certfile, host_name, use_ssl):
    host = host_name
    if use_ssl:
        ssl_opts = {'ca_certs': ca_certs,
                    'keyfile': keyfile,
                    'certfile': certfile,
                    'cert_reqs': ssl.CERT_REQUIRED}
        port = 5671
    else:
        ssl_opts = None
        port = 5672
    parameters = ConnectionParameters(host, port,
        ssl=use_ssl, ssl_options=ssl_opts)
    connection = SelectConnection(parameters, on_connected)

    # Loop until CTRL-C
    try:
        # Start our blocking loop
        connection.ioloop.start()
    except KeyboardInterrupt:
        # Close the connection
        connection.close()
        # Loop until the connection is closed
        connection.ioloop.start()

if __name__ == "__main__":
    simple_server('/home/ikolodyazhny/src/dell/cert-3d/cacert.pem', '/home/ikolodyazhny/src/dell/1/ivan/ivan-key.pem', '/home/ikolodyazhny/src/dell/1/ivan/ivan-cert.pem', '192.168.17.27', True)