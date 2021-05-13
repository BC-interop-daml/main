import json
import logging
import sys
from datetime import date
from os.path import dirname, join
import config
import dazl
from dazl.model.reading import ReadyEvent, ContractCreateEvent

network = dazl.Network()
#Read the name of the template from config.py file
template = config.TEMPLATE_CONGIG["template"]
#Create app.log file
logging.basicConfig(filename='app.log', level=logging.INFO)
def dazl_main (network: network):
    user = config.PARTIES_CONFIG["user"]
    admin = config.PARTIES_CONFIG["admin"]
#User is the signatory of the transaction    
    user = network.aio_party(user)
    global message
#Create smart contract
    @user.ledger_ready()
    def change_owner(event):
#Input the an existed key to search the transaction and the name of the new owner
     key = (input("Type an integer to change car owner by key: "))
     newOwner = str(input("Type a string value for the newowner of the car: "))
     try:
        key =int(key)
        keyCar = 'CAR' + str(key)
      
     except ValueError:
        key =str(key)
        print("The key must be an integer!!!")
        sys.exit()
#Search all transactions by key         
     allContracts = user.find(template = template)
     message = 'There is no match'
     for contract in allContracts:
        if contract.cdata ["keyCar"] == keyCar:
#Exercise option Neowner to change the name of the owner and set previous transaction as archived            
            message = "The car has changed owner"
            print(message)
            print(contract.cdata)
            return dazl.exercise(contract.cid, 'Newowner', {'newOwner': newOwner}) 

            print(contract.cdata)
#A warning that there is no key with the specific key         
     if message == 'There is no match':    
        print(message)                     


def main():
    dazl.run(dazl_main)
        
if __name__ == '__main__':
        main()
