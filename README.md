# automatiq
Intuitive and "cool" CLI that allows you to deploy Health Information Systems with ease. It is as simple as running "deploy <app>" and everything is set up under the hood for you. 


# SET UP
1. # install pip
   sudo apt-get update
   sudo apt-get -y install python3-pip
   pip3 --version

2. # install typer
   pip3 install typer
3. # install paramiko
   pip3 install -U pip
   pip3 install paramiko
   
4. # install sshpass
   sudo apt install sshpass


# Running updates
# updating BHT-EMR-API
  python3 automatiq.py update 1
# updating HIS-Core
  python3 automatiq.py update 2
# update both BHT-EMR-API and HIS-core
  python3 automatiq.py update 0

  [!important notice]
  * make sure that the computer(local) you are using and the targeted computer(server) you have its public ssh key already copied
  * in other words, prior to running the above commands ("#Running updates"), you are able to login into the targedted server via ssh using you computer
