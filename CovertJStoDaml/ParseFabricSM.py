import re
import json
import argparse
import os
from datetime import datetime

#The user is obligated to define cc name
parser = argparse.ArgumentParser(description='Insert Smart Contract Name')
parser.add_argument('--fabric', dest='smartcontractname', type =str, help='Type the name of the smart contract')
args = parser.parse_args()
smartcontractname =args.smartcontractname

#start time monitoring
startTime = datetime.now()

#Removing empty lines from the smart contract
def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)
#Find the Fabric's SM name in order to name the same the daml SM
def find_SM_name(smartcontractname):
    global name
    #Search cc name inside the file
    with open(smartcontractname,) as dataFile:
        data = dataFile.read()
        name = data[data.find('let')+3: data.rfind('= class') -1]
        #Create  empty daml file
        with open(name + (".daml") , 'w') as f:
            startdaml = ("daml 1.2\n" + "module " + name.title() + " where\n")
            f.write(startdaml)
    return (name)
#Split SM name based on the number of the functions
class Writer:
    def __init__(self):
        self._num = 0
        self._fh = None

    def close(self):
        if self._fh:
            self._fh.close()

    def start_file(self):
        self.close()
        self._fh = open("file{}.js".format(self._num), "w")
        self._num += 1
        

    def write(self, data):
        if self._fh:
            self._fh.write(data)

#Finds functions name
def find_functions_names(count):  
    for y in range(0,count):
        #Open the file
        with open("file" + str(y) + ".js") as dataFile:
            #Search the file per line
            for line in dataFile:
                #If the line starts with async means that is a function
                stringToMatchfunctionName = 'async'
                #Keep the name between "async" and "("
                if stringToMatchfunctionName in line:
                    functionsnames = line[line.find('async')+5: line.rfind('(')]


#Find the count and the type of the values for each function                    
def find_args(count):
    name = find_SM_name(smartcontractname)
    matchedLine = ''
    #Open each file seperately 
    for y in range(0,count):
        with open("file" + str(y) + ".js") as dataFile:
            pointer = 0
            for line in dataFile:
                numbers = -1
                values = ""
                #If a line start with "async" then keep the next line 
                stringToMatchfunctionName = 'async'
                if stringToMatchfunctionName in line:
                    functionsnames = line[line.find('async')+5: line.rfind('(')]
                    matchedLine = next(dataFile)
                    #We need to find the line with the word length because is controlled the number of the args
                    matchedvalue = re.search("length",matchedLine)
                    #In case that the functions has an input or more we search for the args name
                    if matchedvalue:
                        values = matchedLine [matchedLine.find('(')+1: matchedLine .rfind('.')]
                        numbers = matchedLine [matchedLine.find("length")+6 : matchedLine.rfind(')')]
                        numbers = numbers.replace("<", "")
                        numbers = numbers.replace("!=","")
                        #Save the count of the args
                        numbers = int(numbers) 
                        #Write name of the founded function on the daml file
                        with open( name + (".daml") , 'a+') as f:
                            writetemplates = ("\ntemplate" + functionsnames.title() + "\n with\n")
                            f.write(writetemplates)
                            f.close()
                    #Functions with no input are written as comments 
                    else:
                        with open( name + (".daml") , 'a+') as f:
                            pointer = 1
                            writetemplates = ("\n--template" + functionsnames.title() + "\n --with\n")
                            f.write(writetemplates)
                            f.close()
                #Search the type of the args
                if values in line:
                    
                    if numbers == -1 :
                        break
                    else:
                        for number in range(numbers):
                            matchedargs = (values + str(number))
                            nextLine = next(dataFile)   
                            #Search if is referred any of this words on the js smart contract 
                            matchStr = re.search("string",nextLine)
                            matchBoolean = re.search("boolean",nextLine)
                            matchBigint = re.search("bigint",nextLine)
                            matchNumstr = re.search("numeric string",nextLine)
                            typevalue = ''
                            if matchStr:
                                typevalue = "string"    
                            elif matchBoolean:
                                typevalue = "boolean"
                            elif matchBigint:
                                typevalue = "bigint"
                            elif matchNumstr:
                                typevalue = "numeric string"
                            else:
                                typevalue = "string"  
                            #Convert the type according to DAML types    
                            with open( name + (".daml") , 'a+') as f:
                                if typevalue == "string":
                                    typevalue = "Text"
                                elif typevalue == "boolean":
                                    typevalue = "Bool"
                                elif typevalue == "numeric string":
                                    typevalue = "Numeric"
                                elif typevalue == "bigint":
                                    typevalue == "Int" 
                                #Write the type and the names of the args 
                                writevalues = ("  " + matchedargs + ":" + typevalue +"\n")  
                                f.write(writevalues)
                                f.close()

        #Add the appropriate daml format                        
        if pointer == 1:
            with open( name + (".daml") , 'a+') as f:   
                writestandards = (" \n --where\n" + "  --signatory\n")  
                f.write(writestandards)
                f.close()
        else:
            with open( name + (".daml") , 'a+') as f:   
                writestandards = (" where\n" + "  signatory\n") 
                f.write(writestandards)
                f.close()                   
                                    
#Delete comments from the smart contract
with open(smartcontractname, "r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "//" in line:
           continue
        if "/*" in line:
            continue
        elif "*/" in line:  
            continue 
        elif "#" in line:  
            continue
        else:
            f.write(line)
    f.truncate()


remove_empty_lines(smartcontractname)
#Call the class to split the SM into multiples files
writer = Writer()
count = 0
with open(smartcontractname) as f:
    for line in f:
        if re.match(' *async ', line):
            count+=1
            writer.start_file()
        writer.write(line)        
    writer.close()

find_functions_names(count) 
find_args(count)    
print ("Your smart contract has been converted! Check the file" + name + ".daml")
print(datetime.now() - startTime)
