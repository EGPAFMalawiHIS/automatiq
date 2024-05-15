# automatiq
Intuitive and "cool" CLI that allows you to deploy Health Information Systems with ease. It is as simple as running "deploy <app>" and everything is set up under the hood for you. 


# SET UP
   
   clone the repository into `/var/www` directory

   while you are in `/var/www/automatiq` directory
   
# install dependencies


       sudo python3 install.py

   after this command:

   do:

       virtualenv venv

       source venv/bin/activate

# Running updates

       python3 update.py


  [!important notice]
  * the app is intended to be installed on the users machine
  * make sure that the computer(local) you are using and the targeted computer(server), you have its public ssh key already copied
  * in other words, Ensure you can access the target host via ssh on the command line before proceeding with the script

  #pictures ..
