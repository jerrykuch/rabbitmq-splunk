#!/usr/bin/python
import sys, os, datetime

# Hack to load splunk packages
#from optparse import OptionParser
#parser = OptionParser()
#(options, args) = parser.parse_args()
#_SPLUNK_PYTHON_PATH = args[0]
#sys.path.append(_SPLUNK_PYTHON_PATH)

#import splunk
#import cherrypy

import pika

#server, port = sys.argv[1].split(":")
server = "ubuntu"
port = "55672"
vhost = "/"
username = "guest"
password = "guest"
#vhost = sys.argv[2]
#username = sys.argv[3]
#password = sys.argv[4]

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

print "%s OK %s connection to %s:%s successful." % (str(now),
                                                    __file__, 
                                                    server, 
                                                    port)
exit(0)
