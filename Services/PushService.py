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

def UpdateHisCore(host: str, username: str, password: str, cmd: str):
    try:
        print("___________________________________________________________________________________________________________________")
        print(" Updating HIS-Core Version")
        print("___________________________________________________________________________________________________________________")

        print("")
        print("Enter IP address of the Facility:")
        try:
            input_ip_address = input("$> ")
        except KeyboardInterrupt:
            print("")
        print("Enter API port the facility uses:")
        try:
            input_api_port = input("$> ")
        except KeyboardInterrupt:
            print("")

        full_cmd = f"{cmd} {input_ip_address} {input_api_port}"
        subprocess.run(full_cmd, shell=True, check=True)
    except Exception as e:
        print(str(e))

@app.command()
def updateVersion(
    app_id: int,
    ip_address: str,
    username: str,
    password: str
):  
    try:
        cmd = ". /var/www/his_core_script.sh"

        if app_id == 1:
            UpdateAPI(ip_address, username, password)

        if app_id == 2:
            UpdateHisCore(ip_address, username, password, cmd)

        if app_id == 0:
            UpdateAPI(ip_address, username, password)
            UpdateHisCore(ip_address, username, password, cmd)

    except Exception as e:
        print("error: ",e)

if __name__ == "__main__":
    app()