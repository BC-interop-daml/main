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
template = config.TEMPLATE_CONFIG["template"]
template2 = config.TEMPLATE2_CONFIG["template2"]
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
    allContractsAuction = client.find(template)
    for contractAuction in allContractsAuction:
        if contractAuction.cdata ["keyCar"] == keyCar:
           foundkey = contractAuction.cdata ["keyCar"]
           print("It is a car for auction" )
           print(contractAuction.cdata)
    allContractsSold = client.find(template2)
    for contractSold in allContractsSold:
        if contractSold.cdata ["keyCar"] == keyCar:
           foundkey = contractSold.cdata ["keyCar"]
           print("It is a sold car" )
           print(contractSold.cdata)           

    #Warning that search by key found no match  
    if foundkey == '':
        sys.exit("There is no car with that key")

if __name__ == '__main__':
    main()
