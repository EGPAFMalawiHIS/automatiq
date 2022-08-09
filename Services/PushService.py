from subprocess import call
from click import command
import typer
import paramiko

app = typer.Typer()

def initParamiko(
    host: str,
    username: str,
    password: str,
    command_to_execute: str
):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout,_stderr = client.exec_command(command_to_execute)
    client.close()

@app.command()
def update_api_versions(
    app_id: int,
    ip_address: str,
    username: str,
    password: str
):
    
    try:
        if app_id == 1:
            cmd = "./ emr_api_script.sh"
            initParamiko(ip_address, username, password, cmd)
        if app_id == 2:
            cmd = "./ his_core_script.sh"
            initParamiko(ip_address, username, password, cmd)
        if app_id == 0:
            cmd = "./ auto_update_script.sh"
            initParamiko(ip_address, username, password, cmd)

    except Exception as e:
        print("error: ",e)