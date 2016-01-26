__author__ = 'cobedien'


import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}
url = "http://198.18.134.17/ins"
username = "admin"
password = "Cisco321"


payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show version',1], 'id': '1'}]
my_data = json.dumps(payload)
response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))


kick_start_image = response.json()['result']['body']['kickstart_ver_str']
system_image = response.json()['result']['body']['kick_file_name']
host_name = response.json()['result']['body']['host_name']
bootflash_size = response.json()['result']['body']['bootflash_size']

print ("")
print ("===============================")
print ('host name:'+ host_name)
print ('kickstart image version :' + kick_start_image)
print ('system image version :s' + system_image)
if bootflash_size > 9991:
	print ('Bootflash size is:' + str(bootflash_size))
print ("===============================")

payload = [{'jsonrpc':'2.0', 'method': 'cli', 'params': ['show int b',1], 'id':'1'}]
my_data2= json.dumps(payload)
response2=requests.post(url, data=my_data2, headers=my_headers, auth=(username, password))
i=0
while i < len (response2.json()['result']['body']['TABLE_interface']['ROW_interface']):
	intf=response2.json()['result']['body']['TABLE_interface']['ROW_interface'][i]
	i=i+1
	if intf['state'] == 'up':
		print intf['interface']

print ("")
print ("==============================")


