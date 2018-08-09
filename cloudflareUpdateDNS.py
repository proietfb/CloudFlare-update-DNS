#!/usr/bin/python

import requests
import json

#My current IP
myCurrentIP = requests.get("https://api.ipify.org").text

#CloudFlare settings
email = <CLOUDFLARE-ACCOUNT-MAIL>
authKey = <CLOUDFLARE-AUTHENTICATION-KEY>
zone = <DOMAIN-NAME>
zoneID = <DOMAIN-ID>
headers = {'X-Auth-Email': email,'X-Auth-Key': authKey, 'Content-type': 'application/json'}
baseURL = 'https://api.cloudflare.com/client/v4{}'

ipUpdated = False

url_path = '/zones/{}/dns_records'.format(zoneID)
r = requests.get(baseURL.format(url_path), headers=headers)

for res in r.json()['result']:
    if res['content'] != myCurrentIP:       
        jsonContent = json.dumps({'type': res['type'], 'name': res['name'], 'content': myCurrentIP, 'proxied': res['proxied']})
        url_path = '/zones/{}/dns_records/{}'.format(zoneID, res['id'])
        url = baseURL.format(url_path)
        requests.put(url, headers = headers, data = jsonContent)
        if not(ipUpdated):
            ipUpdated = True
            with open("myIP.txt",'wr+b') as myIPtxt:    
                if myCurrentIP != myIPtxt.read():
                    myIPtxt.write(myCurrentIP)
