import config
from subprocess import call
import typer
import deploy_fns

app = typer.Typer()

@app.command()
def modules(name: str = typer.Option("", help="Name of a module.")):
    """List of modules that are available for deployment."""

    if name in config.app_modules:
        typer.echo(config.app_modules[name])

    elif name == "":
        for module in config.app_modules:
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
        if name == "api":
            print("Deploying API")
            deploy_fns.update_api(name,version)
        elif name == "core":
            print("Deploying Core")
            deploy_fns.update_core(name,version)

    else:
        typer.echo("Deployment process canceled")   


if __name__ == "__main__":
    app()
