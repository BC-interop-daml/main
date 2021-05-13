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
sawtooth_network = config.PARTIES_CONFIG["network"]
template = config.TEMPLATE_CONGIG["template"]
user = config.PARTIES_CONFIG["user"]
admin = config.PARTIES_CONFIG["admin"]
fabric_network = config.FABRIC_CONFIG ["fabric_network"]
#Create app.log file
logging.basicConfig(filename='app.log', level=logging.INFO)
          
       
network = dazl.Network()
def dazl_main (network: network):
  user_client = network.aio_party(user)
  keysSawtooth = []
  keysFabric = []
  print ("Is starting the process to search keys in Sawtooth")

  with dazl.simple_client(sawtooth_network , user) as client:
    #Parse the key to search for a specific transaction 
    client.ready()
    #Search all contracts
    allContractsSawtooth = client.find(template)
    for contractSawtooth in allContractsSawtooth:
        keysSawtooth.append(contractSawtooth.cdata ["keyCar"]) 

  print ("Is starting the process to search keys in Fabric")      
  with dazl.simple_client(fabric_network, user) as client:
        #Parse the key to search for a specific transaction 
    client.ready()
        #Search all contracts
    allContractsFabric = client.find(template)
    for contractFabric  in allContractsFabric :
        keysFabric.append(contractFabric.cdata ["keyCar"]) 
  print ("Now the transactions are compared based on keys")
  print (keysFabric) 
  print (keysSawtooth)      
  diffkeys =list(set(keysFabric) - set(keysSawtooth))
  print ("The founded keys:")
  print (diffkeys)
  if len(diffkeys) == 0 :
     sys.exit("There is no new transaction")
  else :
    with dazl.simple_client(fabric_network, user) as client:
    #Parse the key to search for a specific transaction 
      client.ready()
      #Search all contracts
      allContractsSawtooth = client.find(template)
      #for x in range(len(diffkeys)):
      #valuekey =diffkeys[x]
      valuekey = ''.join(diffkeys)
      print(valuekey)
      print (type(valuekey))
      for contractSawtooth in allContractsSawtooth:
          if contractSawtooth.cdata ["keyCar"] == valuekey:
            print (valuekey)
            keyCar = contractSawtooth.cdata ["keyCar"]
            color = contractSawtooth.cdata ["color"]
            make = contractSawtooth.cdata ["make"]
            model = contractSawtooth.cdata ["model"]
            owner = contractSawtooth.cdata ["owner"] 
            print (contractSawtooth.cdata)
            #Create smart contract
      @user_client.ledger_ready()
      async def init(event: ReadyEvent):
          print ("Your ledger is updated")
          print (owner)
          print (keyCar)
          print (color)
          print (make)
          print (model)
          createcontract = {'owner':owner, 'keyCar': keyCar, 'color': color, 'make': make, 'model': model, 'user' : user_client.party, 'admin' : admin }
          return dazl.create (template, createcontract)


def main():
  dazl.run(dazl_main)
    
if __name__ == '__main__':
    main()
