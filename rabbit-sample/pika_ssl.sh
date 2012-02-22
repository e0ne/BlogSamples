#!/bin/bash

python runner.py --use_ssl --ca_certs=cacert.pem \
        --keyfile=key.pem \
        --certfile=cert.pem \
        --host=localhost --client=pika
