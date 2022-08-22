#!/usr/bin/env python3
import subprocess

# running system update
PRO_1 = subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE, text=True)

if PRO_1.returncode == 100:
   print("RUN COMMAND USING 'sudo'")

# installing pip 3 for python3
if PRO_1.returncode == 0:
   p2 = subprocess.run(['sudo', 'apt-get', '-y', 'install', 'python3-pip'], stdout=subprocess.PIPE, text=True)
   print(p2.stdout)

   if p2.returncode != 0:
      print(p2.stderr)

   # installing typer
   if p2.returncode == 0:
      p3 = subprocess.run(['pip3', 'install', 'typer'], stdout=subprocess.PIPE, text=True)
      print(p3.stdout)

      if p3.returncode != 0:
         print(p3.stderr)
      
      # installing paramiko
      if p3.returncode == 0:
         p4 = subprocess.run(['pip3', 'install', '-U', 'pip'], stdout=subprocess.PIPE, text=True)
         print(p4.stdout)

         if p4.returncode != 0:
            print(p4.stderr)

         if p4.returncode == 0:
            p5 = subprocess.run(['pip3', 'install', 'paramiko'], stdout=subprocess.PIPE, text=True)
            print(p5.stdout)

            if p5.returncode != 0:
               print(p5.stderr)

            #  installing sshpass for rsync
            if p5.returncode == 0:
               p6 = subprocess.run(['sudo', 'apt', 'install', 'sshpass'], stdout=subprocess.PIPE, text=True)
               print(p6.stdout)

               if p6.returncode != 0:
                  print(p6.stderr)