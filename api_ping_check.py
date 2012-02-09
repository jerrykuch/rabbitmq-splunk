#!/usr/bin/python
import sys
import json, httplib, urllib, base64, socket

# BUGBUG:  Need usage message and option parsing
#  Usage:
#      api_ping_check.py server:port vhost username password
server, port = sys.argv[1].split(":")
vhost = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

conn = httplib.HTTPConnection(server, port)
path = "/api/aliveness-test/%s" % urllib.quote(vhost, safe="")
method = "GET"

credentials = base64.b64encode("%s:%s" % (username, password))

try:
    conn.request(method, path, "",
                 {"Content-Type" : "application/json",
                  "Authorization" : "Basic " + credentials})

except socket.error:
    print "ERROR Could not connect to %s:%s" % (server, port)
    exit(1)
response = conn.getresponse()

if response.status > 299:
    print "ERROR broker failing API aliveness test: status %s %s" % (response.status, response.read())
    exit(1)

print "OK RabbitMQ API ping check, broker %s:%s alive: %s" % (server,port,response.read())
exit(0)
