#! /usr/bin/python

import subprocess
import os
import fileinput

def update_api(dir_name1:str, version:str):
    #dir_name="/var/www/BHT-EMR-API"
    #dir_name2="HIS-Core-release"
    #print ("Entering BHT-EMR-API")
    os.chdir("/var/www/BHT-EMR-API")

    print ("Checkout to latest tag")
    process=subprocess.run(["git", "checkout", version], stdout=subprocess.PIPE)
    print ("Describing Head")
    os.system("git describe HEAD")
    filepath1= "Gemfile.lock"
    if os.path.exists(filepath1):
        os.remove(filepath1)
    else:
        
        print("Can not delete the file as it doesn't exists")
   
    print ("Installing Local Gems")
    os.system("bundle install --local")
    print ("running bin_update art")
    os.system("./bin/update_art_metadata.sh development")


def update_Core(dir_name2:str):
    #print ("=>Changing directory..........")
    os.chdir(dir_name2)
    print ("=>Checkout to latest tag in Core..........")

    print ("=>Describing Head............")
    os.system("git describe HEAD")
    print ("create the configuration file by copying config.json.example to config.json........")
    os.popen('cp config.json.example config.json')
    print ("Configuring IP address and Port in config.json")
    ip_address = input("Enter IP address of the facility: ")
    print(ip_address)
    api_port=input("Enter API port the facility uses: ")
    print(api_port)
    for line in fileinput.input("config.json", inplace=1):
            print (line.replace("0.0.0.0", ip_address), end="")
    for line in fileinput.input("config.json", inplace=1):
            print (line.replace("3000",api_port),end="")

    print ("The following parameters have been ammended in config.json")
    print ("IP address :", ip_address)
    print ("API port   :", api_port)
    print ("THANK YOU")


