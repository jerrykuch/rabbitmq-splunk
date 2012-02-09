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

print "%s actually ran with args %s" % (__file__, sys.argv)
