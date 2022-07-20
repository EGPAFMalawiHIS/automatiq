#! /usr/bin/python

import subprocess
import os
import fileinput
import config
import validation


def update_api(module_name: str, version: str) -> bool:

    if not validation.dir_exist(config.module_dirs[module_name]):
        print("Directory does not exist")
        return False

    os.chdir(config.module_dirs[module_name])

    print("_______________________________________________________________")

    print("Checkout to latest tag")

    process = subprocess.run(["git", "checkout", version], stdout=subprocess.PIPE)

    print("_______________________________________________________________")

    print("Describing Head")

    os.system("git describe HEAD")

    if os.path.exists("Gemfile.lock"):

        os.remove("Gemfile.lock")

    else:

        print("Can not delete the file as it doesn't exists")
        print("_______________________________________________________________")

    print("Installing Local Gems")

    os.system("bundle install --local")

    print("running bin_update art")

    print("_______________________________________________________________")

    os.system("./bin/update_art_metadata.sh development")

    return True


def update_core(module_name: str, version: str) -> bool:

    # print ("=>Changing directory..........")
    os.chdir(config.module_dirs[module_name])
    print("Checkout to latest tag in Core..........")

    print("_______________________________________________________________")

    print("Describing Head")

    print("_______________________________________________________________")

    os.system("git describe HEAD")
    print(
        "create the configuration file by copying config.json.example to config.json........"
    )
    print("_______________________________________________________________")

    os.popen("cp config.json.example config.json")
    print("Configuring IP address and Port in config.json")
    ip_address = input("Enter IP address of the facility: ")
    print(ip_address)
    api_port = input("Enter API port the facility uses: ")
    print(api_port)
    for line in fileinput.input("config.json", inplace=1):
        print(line.replace("0.0.0.0", ip_address), end="")
    for line in fileinput.input("config.json", inplace=1):
        print(line.replace("3000", api_port), end="")

    print("_______________________________________________________________")
    print("The following parameters have been ammended in config.json")
    print("_______________________________________________________________")

    print("IP address :", ip_address)
    print("_______________________________________________________________")

    print("API port   :", api_port)
    print("_______________________________________________________________")

    print("THANK YOU")

    return True
