# automatiq
Intuitive and "cool" CLI that allows you to deploy Health Information Systems with ease. It is as simple as running "deploy <app>" and everything is set up under the hood for you. 


sudo apt install sshpass

#SET UP
1. # install typer
   pip install "typer[all]"
   
2. # instll sshpass
   sudo apt install sshpass

# Running updates
# updating BHT-EMR-API
  python3 automatiq.py update 1
# updating HIS-Core
  python3 automatiq.py update 2
# update both BHT-EMR-API and HIS-core
  python3 automatiq,py update 0