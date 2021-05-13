import json
import logging
import sys
import argparse
from datetime import date
from os.path import dirname, join
import config
import dazl
from dazl.model.reading import ReadyEvent, ContractCreateEvent

#Read values from config.py file
network = config.PARTIES_CONFIG["network"]
template = config.TEMPLATE_CONFIG["template"]
user = config.PARTIES_CONFIG["user"]
admin = config.PARTIES_CONFIG["admin"]
#Create app.log file
logging.basicConfig(filename='app.log', level=logging.INFO)

network = dazl.Network()
def create_car (network: network, keyCar, color, make, model, owner, admin, user):
 user_client = network.aio_party(user)
 
 #Create smart contract
 @user_client.ledger_ready()

 async def init(event: ReadyEvent):
#Search all contracts for a existed key 
  #global foundkey
  #foundkey = '' 
  allContracts =user_client.find(template = template)
  for contract in allContracts:
#If the key already exist the user can choose to try with another key or just leave
      if contract.cdata ["keyCar"] == keyCar:
        foundkey = contract.cdata ["keyCar"]
        message = 'This key already exists '
        print (message,foundkey)
        sys.exit("Is impossible to duplicate a key...try again")

  #if foundkey == '':
  print ("You have deployed a new transaction")
  createcontract = {'owner':owner, 'keyCar': keyCar, 'color': color, 'make': make, 'model': model, 'user' : user_client.party, 'admin' : admin }
  return dazl.create (template, createcontract)
  #else:
    #print("You cannot make an entry with ", foundkey, " because alreasy exists")


def dazl_main(network):
#User inputs values     

    color = str(input("Type a string value for the color of the car: "))
    make = str(input("Type a string value for the maker of the car: "))
    model = str(input("Type a string value for the model of the car: "))
    owner = str(input("Type a string value for the owner of the car: "))
    key = (input("Type an integer to create a key for you transactions: "))
#Evaluate key of the transaction    
    try:
      key =int(key)
      keyCar = 'CAR' + str(key)
      
    except ValueError:
      key =str(key)
      print("The key must be an integer!!!")
      sys.exit()

    create_car(network, keyCar, color, make, model, owner, user, admin)


def main():
  dazl.run(dazl_main)
    
if __name__ == '__main__':
    main()
