# BC-interop-daml
# A Portable DAML application on Fabric network & Sawtooth network

FabcCar app implementation of DAML ledger that stores data transactions using Hyperledger Fabric & Hyperledger Sawtooth. 

# Quick Start Guide

## Prerequisites

These are the minimal requirements that this flow was tested with. It's good to use greater versions or sometimes even lower, but not advised.
- **Ubuntu** version 18.04
- **Python** version > 3.6
- **Dazl** version > 7.5
- **Pipenv**
- **DAML SDK** version > 0.13.40

### Deploy DAML FabCar smart contract on Hyperledger Fabric

### Step 1. Setup & Start Hyperledger Fabric Network

repo: https://github.com/digital-asset/daml-on-fabric

### Step 2. Install DAML Smart Contract on HLF network

Path for DAML FabCar SC: HLF_FabCar_SC_DAML/daml/FabCar.daml


### Step 3. Interact with python app

```
$ cd HLF_FabCar_SC_DAML/Fabric/Python
```

```
$ pipenv run python3 InitLedger.py --url http://localhost:6865
```

```
$ pipenv run python3 ChangeOwner.py --url http://localhost:6865
```

```
$ pipenv run python3 CreateCar.py --url http://localhost:6865
```

```
$ pipenv run python3 QueryAllCars.py 
```

```
$ pipenv run python3 QueryCarbyKey.py --key <int value>
```

### Step 4. Conclusion

Now you can explore your freshly setup DAML ledger.

You should have the following services running:

- DAML Navigator at http://localhost:7500/
- Hyperledger Fabric block explorer at http://localhost:8080/blocks
- Hyperledger Fabric block explorer at http://localhost:8080/transactions
- DAML Ledger API endpoint at *localhost:6865*

### Deploy DAML FabCar smart contract on Hyperledger Sawtooth

### 1. Setup & Start Hyperlegder Sawtooth network

repo: https://github.com/blockchaintp/daml-on-sawtooth


### Step 2. Install DAML Smart Contract on HLF network

Path for DAML FabCar SC: HLF_FabCar_SC_DAML/daml/FabCar.daml


### Step 3. Interact with python app

```
$ cd HLF_FabCar_SC_DAML/Sawtooth/Python
```

```
$ pipenv run python3 InitLedger.py --url http://localhost:9000
```

```
$ pipenv run python3 ChangeOwner.py --url http://localhost:9000
```

```
$ pipenv run python3 CreateCar.py --url http://localhost:9000
```

```
$ pipenv run python3 QueryAllCars.py 
```

```
$ pipenv run python3 QueryCarbyKey.py --key <int value>
```

### Step 4. Conclusion

Now you can explore your freshly setup DAML ledger.

You should have the following services running:

- DAML Navigator at http://localhost:4000/
- Hyperledger Fabric block explorer at http://localhost:80/
- DAML Ledger API endpoint at *localhost:9000*

# An interoperable approach for DAML app on Fabric network & Sawtooth network

FabcCar app implementation of DAML ledger that stores data transactions using Hyperledger Fabric & Hyperledger Sawtooth


# Quick Start Guide


### Deploy DAML FabCar smart contract on Hyperledger Fabric
### Step 1. Setup & Start Hyperledger Fabric Network

repo: https://github.com/digital-asset/daml-on-fabric

### Step 2. Install DAML Smart Contract on HLF network

Path for DAML FabCar SC: DAML-Relays/SMFabric/daml/FabCar.daml

### Step 3. Interact with python libraries

```
$ cd /DAML-Relays/Fabric/Python
```

```
$ pipenv run python3 InitLedger.py --url http://localhost:6865
```

```
$ pipenv run python3 ChangeOwner.py --url http://localhost:6865
```

```
$ pipenv run python3 CreateCar.py --url http://localhost:6865
```

```
$ pipenv run python3 QueryAllCars.py 
```

```
$ pipenv run python3 QueryCarbyKey.py --key <int value>
```

### Step 4. Conclusion

Now you can explore your freshly setup DAML ledger.

You should have the following services running:

- DAML Navigator at http://localhost:7500/
- Hyperledger Fabric block explorer at http://localhost:8080/blocks
- Hyperledger Fabric block explorer at http://localhost:8080/transactions
- DAML Ledger API endpoint at *localhost:6865*

### Deploy DAML FabCar smart contract on Hyperledger Sawtooth

### 1. Setup & Start Hyperlegder Sawtooth network

repo: https://github.com/blockchaintp/daml-on-sawtooth


### Step 2. Install DAML Smart Contract on HLF network

Path for DAML FabCar SC: DAML-Relays/SMSAwtooth/daml/FabCar.daml


### Step 3. Interact with python app

```
$ cd /DAML-Relays/Sawtooth/Python
```

```
$ pipenv run python3 QueryAllCars.py 
```

```
$ pipenv run python3 QueryCarbyKey.py --key <int value>
```

### Step 4. Conclusion

Now you can explore your freshly setup DAML ledger.

You should have the following services running:

- DAML Navigator at http://localhost:4000/
- Hyperledger Fabric block explorer at http://localhost:80/
- DAML Ledger API endpoint at *localhost:9000*

# Reverse Engineering - Convertion of a HLF node.js chaincode to DAML smart contract
## Prerequisites
- **Python** version > 3.6

 Python libralies:
- **re**
- **json**
- **argparse** 
- **os**
- **datetime** 

Convert a HLF node.js to DAML. The format of the chaincode should be based on the example

# Quick Start Guide

### Step 1. Navigate to the CovertJStoDaml folder and add a new SC or test the marbles.js chaincode

```
$ cd ../CovertJStoDaml
```
### Step 2. Concert the chaincode to DAML smart contract

```
$ python3 ParseFabricSM.py --fabric marbles.js
```
# License

Code is available under the GPL 3.0 license

https://www.gnu.org/licenses/gpl-3.0.html

