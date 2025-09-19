import os
import urllib.request as urllib2
import json
import sys

if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    ip = input("What is your target IP: ")

url = "http://ip-api.com/json/"
response = urllib2.urlopen(url + ip)
data = response.read()
values = json.loads(data)

print("IP: " + values["query"])
print("City: " + values["city"])
print("ISP: " + values["isp"])
print("Country: " + values["country"])
print("Region: " + values["region"])
print("Timezone: " + values["timezone"])