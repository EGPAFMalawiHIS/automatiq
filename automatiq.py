import lang
from subprocess import call
import typer

app = typer.Typer()

@app.command()
def modules(name: str = typer.Option("", help="Name of a module.")):
    """List of modules that are available for deployment."""

    if name in lang.app_modules:
        typer.echo(lang.app_modules[name])

    elif name == "":
        for module in lang.app_modules:
            typer.echo(module)

    else:
        typer.echo("Module not found")

@app.command()
def deploy(
    name: str,
    version: str,
    force: bool = typer.Option(..., prompt="Are you sure you want to deploy the module?"),
):
    if force:
        typer.echo(f"Deploying {name} version {version}")
        runner = call("./auto_update_script.sh", shell=True)
    else:
        typer.echo("Deployment process canceled")   

@app.command()
def update(
    app_id: int
):
    try: 
        if app_id == 1:
            call("./UpdateScripts/auto_update_emr_api.sh")
        if app_id == 2:
            call("./UpdateScripts/auto_update_his_core.sh")
        if app_id == 0:
            call("./UpdateScripts/auto_update_both_modules.sh")
    except Exception as e:
        print("error: ",e)

if __name__ == "__main__":
    app()
