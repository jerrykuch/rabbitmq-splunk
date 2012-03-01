#!/usr/bin/python
import sys, datetime
import json, httplib, urllib, base64, socket

# BUGBUG:  Need usage message and option parsing
#  Usage:
#      queue_integrity_check server:port vhost username password \
#                            queuename is_durable is_auto_delete
#
server, port = sys.argv[1].split(":")
vhost = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
queue_name = sys.argv[5]
is_durable = json.loads(sys.argv[6].lower())
is_auto_delete = json.loads(sys.argv[7].lower())

conn = httplib.HTTPConnection(server, port)
path = "/api/queues/%s/%s" % (urllib.quote(vhost, safe=""),
                              urllib.quote(queue_name))
method = "GET"

credentials = base64.b64encode("%s:%s" % (username, password))

try:
    now = datetime.datetime.now()
    conn.request(method, path, "",
                 {"Content-Type" : "application/json",
                  "Authorization" : "Basic " + credentials})

except socket.error:
    print "ERROR Could not connect to %s:%s" % (server, port)
    exit(1)

response = conn.getresponse()

# Check salient error codes...
if response.status == 404:
    print "ERROR queue %s does not exist." % (queue_name)
    exit(1)
elif response.status > 299:
    print "ERROR unexpected API error %s checking queue %s" % (response.status,
                                                               queue_name)
    exit(1)

print "response.status = %s" % response.status
#print ">>>>\n%s\n" % response.read()

response = json.loads(response.read())

if response["auto_delete"] != is_auto_delete:
    print "ERROR queue %s auto_delete flag is not %s as expected." % (queue_name,
                                                                      is_auto_delete)
    exit(1)

if response["durable"] != is_durable:
    print "ERROR queue %s durable flag is not %s as expected." % (queue_name,
                                                                  is_durable)
    exit(1)

print "OK queue %s configured correctly." % queue_name
exit(0)
