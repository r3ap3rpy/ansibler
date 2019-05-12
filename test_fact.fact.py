#!/usr/bin/python
import requests
import json
print json.dumps({'public_ip':str(requests.get("http://whatismyip.akamai.com").text)})