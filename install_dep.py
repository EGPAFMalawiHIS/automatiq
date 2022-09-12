#!/usr/bin/env python3
import subprocess

#
dependencies_list = [
   'sudo apt-get update',
   'sudo apt-get -y install python3-pip',
   'pip3 install typer',
   'pip3 install -U pip',
   'pip3 install paramiko',
   'sudo apt-get install sshpass'
]

for dependency in dependencies_list:
   print("____________________________________________________________________________________________")
   print(dependency)
   print("............................................................................................")
   _process = subprocess.run(dependency.split(), stdout=subprocess.PIPE)
   print(_process.stdout)

   if _process.returncode != 0:
      print(_process.stderr)