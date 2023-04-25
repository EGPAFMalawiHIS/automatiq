from click import command
import typer
import paramiko
import subprocess

app = typer.Typer()

def UpdateAPI(host: str, username: str, password: str):
    print("___________________________________________________________________________________________________________________")
    print(" Updating EMR-API Version")
    print("___________________________________________________________________________________________________________________")
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    
    # define the commands to run in sequence
    commands = [
        'cd /var/www/BHT-EMR-API && pwd',
        'cd /var/www/BHT-EMR-API && git checkout v4.17.1 -f',
        'cd /var/www/BHT-EMR-API && git describe',
        'cd /var/www/BHT-EMR-API && git describe > HEAD',
        'cd /var/www/BHT-EMR-API && rm Gemfile.lock',
        'cd /var/www/BHT-EMR-API && bundle install --local'
    ]
    
    for cmd in commands:
        # run the command using subprocess
        subprocess.run(cmd, shell=True, check=True)
        print("___________________________________________________________________________________________________________________")
 
    client.close()

def UpdateHisCore(host: str, username: str, password: str):
    print("___________________________________________________________________________________________________________________")
    print(" Updating HIS-Core Version")
    print("___________________________________________________________________________________________________________________")
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)

    # prompt user for IP address and port number
    ip = input("Enter API IP address: ")
    port = input("Enter API port number: ")

    # copy or modify config.json.example to config.json with user input
    # check localhost and 3000 if it exists like below
    # "apiURL": "localhost",
	# "apiPort": "3000",
    commands = [
        f'cd /var/www/HIS-Core && cp config.json.example config.json',
        f'sed -i \'s/"apiURL": "localhost",/"apiURL": "{ip}",/\' /var/www/HIS-Core/config.json',
        f'sed -i \'s/"apiPort": "3000",/"apiPort": "{port}",/\' /var/www/HIS-Core/config.json'
    ]

    commands += [
        'cd /var/www/HIS-Core && git checkout v1.8.2 -f',
        'cd /var/www/HIS-Core && git describe > HEAD',
    ]

    for cmd in commands:
        # run the command using subprocess
        subprocess.run(cmd, shell=True, check=True)
        print("___________________________________________________________________________________________________________________")

    client.close()


@app.command()
def updateVersion(app_id: int, ip_address: str, username: str, password: str):  
    try:
        if app_id == 1:
            UpdateAPI(ip_address, username, password)

        if app_id == 2:
            UpdateHisCore(ip_address, username, password)

        if app_id == 0:
            UpdateAPI(ip_address, username, password)
            UpdateHisCore(ip_address, username, password)

    except Exception as e:
        print("error: ",e)

if __name__ == "__main__":
    app()