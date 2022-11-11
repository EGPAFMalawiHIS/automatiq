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
    print("___________________________________________________________________________________________________________________")
    print(cmd.capitalize())
    print("___________________________________________________________________________________________________________________")
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    cmd = "echo $PATH; cd /var/www/BHT-EMR-API; /bin/bash --login -c \""+cmd+"\""
    _stdin, _stdout,_stderr = client.exec_command(cmd)
    print ("stderr: ", _stderr.readlines())
    print ("pwd: ", _stdout.readlines())
    client.close()

def initParamikoForHisCore(
    host: str,
    username: str,
    password: str,
    cmd: str
):
    try:
        print(" executing update versions script")
        client = paramiko.client.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        print("###################################################")
        print("########## Changing HIS-Core Version ##############")
        print("###################################################")
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

        try:
            _stdin, _stdout,_stderr = client.exec_command(cmd+" "+input_ip_address+" "+input_api_port)
            print ("stderr: ", _stderr.readlines())
            print ("pwd: ", _stdout.readlines())
        except Exception as e:
            print(str(e))

        client.close()
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
        emr_api_cmds = [
            '. /var/www/emr_api_script.sh',
            './bin/update_art_metadata.sh development'
        ]
        if app_id == 1:
            for cmd in emr_api_cmds:
                initParamiko(ip_address, username, password, cmd)
        if app_id == 2:
            cmd = ". /var/www/his_core_script.sh"
            initParamikoForHisCore(ip_address, username, password, cmd)
        if app_id == 0:
            for cmd in emr_api_cmds:
                initParamiko(ip_address, username, password, cmd)
            cmd2 = ". /var/www/his_core_script.sh"
            initParamikoForHisCore(ip_address, username, password, cmd2)

    except Exception as e:
        print("error: ",e)

if __name__ == "__main__":
    app()