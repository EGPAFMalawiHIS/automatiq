from click import command
import typer
import paramiko
import subprocess
import json

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

    # check if config.json file exists
    stdin, stdout, stderr = client.exec_command('ls /var/www/HIS-Core')
    files = stdout.readlines()
    if 'config.json\n' not in files:
        print('Error: config.json file not found in /var/www/HIS-Core directory')
        print('copied config.json.example config.json')
        subprocess.run('cd /var/www/HIS-Core && cp config.json.example config.json', shell=True, check=True)

    
    # extract apiURL and apiPort values from config.json
    stdin, stdout, stderr = client.exec_command('cat /var/www/HIS-Core/config.json')
    config_str = stdout.read().decode('utf-8')
    config = json.loads(config_str)
    current_ip = config['apiURL']
    current_port = config['apiPort']

    commands = []
    # prompt user to keep or change API IP address and port number
    keep_current = input(f'Current API IP: {current_ip}, Port: {current_port}, in config.json. Do you want to change these values? (y/n): ')
    if keep_current.lower() == 'y':
        ip = input("Enter new API IP address: ")
        port = input("Enter new API port number: ")
    else:
        ip = current_ip
        port = current_port

    # modify config.json with user input
    if keep_current.lower() == 'y':
        commands = [
            f'cd /var/www/HIS-Core && cp config.json.example config.json',
            f'sed -i \'s/"apiURL": "{current_ip}",/"apiURL": "{ip}",/\' /var/www/HIS-Core/config.json',
            f'sed -i \'s/"apiPort": "{current_port}",/"apiPort": "{port}",/\' /var/www/HIS-Core/config.json'
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
        print("Error:", e)

if __name__ == "__main__":
    app()