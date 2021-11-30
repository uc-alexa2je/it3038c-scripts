import requests
import json




r = requests.get("http://localhost:3000")
data = r.json()

widgetNo = int(input())

for d in data:
    print("%s is %s" % (d['name'], d['color']))
