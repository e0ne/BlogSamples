import os
import sys
import getopt

from kombu_sample.simple import simple_queue
from pika_sample.server import simple_server

def main():
    use_ssl = False
    ca_certs = ''
    keyfile = ''
    certfile = ''
    host = 'localhost'
    client = ''
    path = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], None, [
                                                        'ca_certs=',
                                                        'keyfile=',
                                                        'certfile=',
                                                        'host=',
                                                        'client=',
                                                        'dir='
                                                        'use_ssl',
                                                        'help'
        ])

        for o, a in opts:
            if o in ('--ca_certs'):
                ca_certs = a
            elif o in ('--keyfile'):
                keyfile = a
            elif o in ('--certfile'):
                certfile = a
            elif o in ('--host'):
                host = a
            elif o in ('--client'):
                client = a
            elif o in ('--path'):
                path = a
            elif o in ('--help'):
                printHelp()
                sys.exit(0)
            elif o in ('--use_ssl'):
                    use_ssl = True
        if path:
            ca_certs, keyfile, certfile = parse_direcroty(path)
        if client == 'kombu':
            create_kombu_queue(ca_certs, keyfile, certfile, host, use_ssl)
        else:
            create_pika_queue(ca_certs, keyfile, certfile, host, use_ssl)

    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

def printHelp():
    print 'Arguments help will be here.'

def create_kombu_queue(ca_certs, keyfile, certfile, host, use_ssl):
    simple_queue(ca_certs, keyfile, certfile, host, use_ssl)

def create_pika_queue(ca_certs, keyfile, certfile, host, use_ssl):
    simple_server(ca_certs, keyfile, certfile, host, use_ssl)

def parse_direcroty(path):
    ca_certs = None
    keyfile = None
    certfile = None
    for file in os.listdir(path):
        if file.endswith('-key.pem'):
            keyfile = file
        elif file.endswith('-cert.pem'):
            certfile = file
        elif file.endswith('cacert.pem'):
            ca_certs = file
    return ca_certs, keyfile, certfile
if __name__ == '__main__':
    main()