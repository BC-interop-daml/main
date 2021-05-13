import csv
import pandas as pd
import numpy
import json
import logging
import os
import sys
import time
from datetime import date
from os.path import dirname, join
from configparser import SafeConfigParser
import dazl
import config
from dazl.model.reading import ReadyEvent, ContractCreateEvent
#Read values from ini file
network = dazl.Network()
parser = SafeConfigParser()
parser.read('configvalues.ini')
network = parser.get('url_value','url')
csv_name = parser.get('csv_value','csvname')
#network.set_config(url=network)
#Read values from config.py file
user = config.PARTIES_CONFIG["user"]
admin = config.PARTIES_CONFIG["admin"]
template = config.TEMPLATE_CONFIG["template"]
#Create app.log file
logging.basicConfig(filename='app.log', level=logging.INFO)

def init_ledger (network: dazl.Network, keyCar, color, make, model, owner, user, admin, x):
 user_client = network.aio_party(user)
 #Create smart contract
 @user_client.ledger_ready()
 async def init(event: ReadyEvent):
		allcontracts = user_client.find(template = template)
		for contract in allcontracts:
				if contract.cdata ["keyCar"] == keyCar:
						sys.exit("The key " + keyCar + " already exists...is impossible to duplicate a key")
	 #Initilizing transactions from csv
				logging.info ("Initializing car for " + owner)
				#Set values according to template of smart contract
		initcontract = {'owner':owner, 'keyCar': keyCar, 'color': color, 'make': make, 'model': model, 'user' : user_client.party, 'admin' : admin }
		return dazl.create (template, initcontract)  

def dazl_main(network):
#Read values from csv
		with open(csv_name) as csvfile:
		 readCSV = csv.reader(csvfile, delimiter=',')
		 x = 0
		 for row in readCSV:
				color = row[0]
				make = row[1]
				model = row[2]
				owner = row[3]
#Create a key for the transactions
				keyCar = "CAR" + str(x)
				init_ledger(network, keyCar, color, make, model, owner, user, admin, x)
				x = x+1

#Dazl deploys transcactions
def main():
	dazl.run(dazl_main)
		
if __name__ == '__main__':
		main()
