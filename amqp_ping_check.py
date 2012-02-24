#!/usr/bin/python
import sys, os, datetime
import pika

# BUGBUG:  Need usage message and option parsing
#  Usage:
#      amqp_ping_check.py server:port vhost username password
server, port = sys.argv[1].split(":")
vhost = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

creds_broker = pika.PlainCredentials(username, password)
conn_params = pika.ConnectionParameters(server,
                                        virtual_host = vhost,
                                        credentials = creds_broker)
try:
    now = datetime.datetime.now()
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()
except Exception:
    print "%s ERROR %s could not connect to %s:%s!" % (str(now),
                                                       __file__,
                                                       server,
                                                       port)
    exit(1)

print "%s OK RabbitMQ AMQP ping check, broker %s:%s alive." % (str(now),
                                                               server,
                                                               port)
exit(0)
