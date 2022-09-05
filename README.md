# automatiq
Intuitive and "cool" CLI that allows you to deploy Health Information Systems with ease. It is as simple as running "deploy <app>" and everything is set up under the hood for you. 


# SET UP
   
   clone the repository into `/var/www` directory

   while you are in `/var/www/automatiq` directory
1. install dependencies
   sudo python3 install_dep.py

# Running updates
  updating BHT-EMR-API
  python3 automatiq.py update 1

  updating HIS-Core
  python3 automatiq.py update 2

  update both BHT-EMR-API and HIS-core
  python3 automatiq.py update 0

  [!important notice]
  * the is intended to be installed on the users machine
  * make sure that the computer(local) you are using and the targeted computer(server), you have its public ssh key already copied
  * in other words, Ensure you can access the target host via ssh on the command line before proceeding with the script