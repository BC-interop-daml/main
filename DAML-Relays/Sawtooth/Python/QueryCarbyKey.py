import json
import os
import dazl
import logging
import sys
import argparse
from asyncio import sleep
import config
import dazl

network = config.PARTIES_CONFIG["network"]
user = config.PARTIES_CONFIG["user"]
template = config.TEMPLATE_CONGIG["template"]
global foundkey
foundkey = ''
def main():
 with dazl.simple_client(network, user) as client:
    #Parse the key to search for a specific transaction
    parser = argparse.ArgumentParser(description='Create a transaction for a new car')
    parser.add_argument('--key', help='Type an integer to create a key for you transactions', type=int, required=True)
    args = vars(parser.parse_args())  
    key = args['key']
    keyCar = "CAR" + str(key) 
    global foundkey
    foundkey = '' 
    client.ready()
    #Search all contracts
    allContracts = client.find(template)
    for contract in allContracts:
        if contract.cdata ["keyCar"] == keyCar:
           foundkey = contract.cdata ["keyCar"]
           print("The query is" )
           print(contract.cdata)

    #Warning that search by key found no match  
    if foundkey == '':
        sys.exit("There is no car with that key")

if __name__ == '__main__':
    main()
