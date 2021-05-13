import json
import os
import dazl
import config
#Read the url and the signatory from config.py file
network = config.PARTIES_CONFIG["network"]
user = config.PARTIES_CONFIG["user"]

def main():
    with dazl.simple_client(network, user) as client:
    #Print all the active transaction without any condition
      client.ready()
      contract_dict = client.find_active('*')
    print(contract_dict)
    print('It is done')

if __name__ == '__main__':
 main()
