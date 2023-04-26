from click import command
import typer
import paramiko
import json
import time
import os
import paramiko

app = typer.Typer()

def find_remote_bundle_dir(username, hostname, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    home_dir = ssh.exec_command("echo $HOME")[1].read().decode().strip()
    bundle_dir = os.path.join(home_dir)
    command = f"find {bundle_dir} -name bundle"
    stdin, stdout, stderr = ssh.exec_command(command)
    results = stdout.readlines()
    results = [result.strip() for result in results]
    
    matching_dirs = []
    for bundle_dir in results:
        command = f"grep -liE 'rvm|rbenv' {bundle_dir}/*"
        stdin, stdout, stderr = ssh.exec_command(command)
        rvm_rbenv_found = any(['rvm' in line.lower() or 'rbenv' in line.lower() for line in stdout.readlines()])
        if not rvm_rbenv_found:
            matching_dirs.append(bundle_dir)
    
    return matching_dirs

def UpdateAPI(host: str, username: str, password: str):
    # print(find_remote_bundle_dir(hostname=host, username=username, password=password))
    print("___________________________________________________________________________________________________________________")
    print(" Updating EMR-API Version")
    print("___________________________________________________________________________________________________________________")
    ssh = paramiko.SSHClient()
    # ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    
    # define the commands to run in sequence
    commands = [
        'whoami',
        'cd /var/www/BHT-EMR-API && pwd',
        'cd /var/www/BHT-EMR-API && git checkout v4.17.1 -f',
        'cd /var/www/BHT-EMR-API && git describe',
        'cd /var/www/BHT-EMR-API && git describe > HEAD',
        'cd /var/www/BHT-EMR-API && rm Gemfile.lock',
    ]
    
    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # while not stdout.channel.exit_status_ready():
        #     time.sleep(1)

        for line in stdout.read().decode('utf-8').splitlines():
            print(line)

        for line in stderr.read().decode('utf-8').splitlines():
            print(line)
        print("___________________________________________________________________________________________________________________")

    remote_bundle_dirs = find_remote_bundle_dir(hostname=host, username=username, password=password)

    print(f"Found {len(remote_bundle_dirs)} bundle directories on the remote server:")

    for bundle_dir in remote_bundle_dirs:
        print(f"- {bundle_dir}")

    # Try each bundle path and see if it works
    for bundle_path in remote_bundle_dirs:
        bundle_install_cmd = f"cd /var/www/BHT-EMR-API && {bundle_path} install --local"
        print(f"Trying bundle path {bundle_path}...")
        print(bundle_install_cmd)

        stdin, stdout, stderr = ssh.exec_command(bundle_install_cmd)
        for line in stdout.read().decode('utf-8').splitlines():
            print(line)
        for line in stderr.read().decode('utf-8').splitlines():
            print(line)

        # Check the exit status of the command to see if it was successful
        if stdout.channel.recv_exit_status() == 0:
            print(f"Successfully installed bundles using {bundle_path}")
            break
        else:
            print(f"Failed to install bundles using {bundle_path}")

    ssh.close()

def UpdateHisCore(host: str, username: str, password: str):
    print("___________________________________________________________________________________________________________________")
    print(" Updating HIS-Core Version")
    print("___________________________________________________________________________________________________________________")
    ssh = paramiko.SSHClient()
    # client.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)

    # check if config.json file exists
    stdin, stdout, stderr = ssh.exec_command('ls /var/www/HIS-Core')
    files = stdout.readlines()
    if 'config.json\n' not in files:
        print('Error: config.json file not found in /var/www/HIS-Core directory')
        print('copied config.json.example config.json')
        ssh.exec_command('cd /var/www/HIS-Core && cp config.json.example config.json')

    
    # extract apiURL and apiPort values from config.json
    stdin, stdout, stderr = ssh.exec_command('cat /var/www/HIS-Core/config.json')
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
        print(port)
        print(ip)
        commands = [
            f'cd /var/www/HIS-Core && cp config.json.example config.json',
            f'sed -i \'s/"apiURL": "{current_ip}",/"apiURL": "{ip}",/\' /var/www/HIS-Core/config.json',
            f'sed -i \'s/"apiPort": "{current_port}",/"apiPort": "{port}",/\' /var/www/HIS-Core/config.json'
        ]

    commands += [
        f'cd /var/www/HIS-Core && git checkout v1.8.2 -f',
        f'cd /var/www/HIS-Core && git describe',
        f'cd /var/www/HIS-Core && git describe > HEAD',
    ]

    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        for line in stdout.read().decode('utf-8').splitlines():
            print(line)

        print("___________________________________________________________________________________________________________________")

    ssh.close()


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