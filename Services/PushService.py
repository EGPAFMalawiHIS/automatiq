from click import command
import typer
import paramiko

app = typer.Typer()

def initParamiko(
    host: str,
    username: str,
    password: str,
    cmd: str
):
    print(" executing update versions script")
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout,_stderr = client.exec_command(cmd)
    print ("stderr: ", _stderr.readlines())
    print ("pwd: ", _stdout.readlines())
    client.close()

@app.command()
def updateVersion(
    app_id: int,
    ip_address: str,
    username: str,
    password: str
):  
    try:
        if app_id == 1:
            cmd = ". /var/www/emr_api_script.sh"
            initParamiko(ip_address, username, password, cmd)
        if app_id == 2:
            cmd = ". /var/www/his_core_script.sh"
            initParamiko(ip_address, username, password, cmd)
        if app_id == 0:
            cmd = ". /var/www/auto_update_script.sh"
            initParamiko(ip_address, username, password, cmd)

    except Exception as e:
        print("error: ",e)

if __name__ == "__main__":
    app()