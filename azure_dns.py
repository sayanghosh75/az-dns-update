#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 7 2022

@author: Sayan A Ghosh
"""

from azure.mgmt.dns import DnsManagementClient
from azure.common.credentials import UserPassCredentials
from azure.identity import DefaultAzureCredential, ClientSecretCredential
import requests

# Replace this with your subscription id
subscription_id = '<update your subscription ID>'
tenant_id = '<update your tenant id>'
client_id = '<update your client id>'
client_secret = '<update your client secret>'
credentials = ClientSecretCredential(tenant_id, client_id, client_secret)

dns_client = DnsManagementClient(
	credentials,
	subscription_id
)

api_endpoint = "https://sayan-tech-api-py.azurewebsites.net/api/"
api_call = "myip"
header = {"accept": "*/*"}
try:
    response = requests.get(api_endpoint+api_call, headers=header)
except:
    print("API Connection error")
if response.status_code == 200:
    source_ip = response.content.decode('utf-8')
print(source_ip)

record_set = dns_client.record_sets.create_or_update(
	'Common',
	'<update your DNS zone>',
	'<update your host>',
	'A',
	{
			"ttl": 300,
			"arecords": [
				{
				"ipv4_address": source_ip
				}
			]
	}
)
