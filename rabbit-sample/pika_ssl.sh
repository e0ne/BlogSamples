#!/bin/bash

python runner.py --use_ssl --ca_certs=/home/ikolodyazhny/src/dell/cert-3d/cacert.pem \
        --keyfile=/home/ikolodyazhny/src/dell/1/ivan/ivan-key.pem \
        --certfile=/home/ikolodyazhny/src/dell/1/ivan/ivan-cert.pem \
        --host=192.168.17.27 --client=pika
