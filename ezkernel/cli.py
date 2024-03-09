import typer
from ezkernel import KernelManager
import sys
app = typer.Typer(invoke_without_command=True, no_args_is_help=True, help="ezkernel is a CLI for managing Jupyter kernels.")
kernel_manager = KernelManager()

@app.callback()
def callback():
    """
    ezkernel is a Python library for managing Jupyter kernels.

    With ezkernel, you can easily add, remove, and rename Jupyter kernels directly from the command line.
    """

@app.command()
def list():
    """List all available Jupyter kernels."""
    kernels = kernel_manager.list_kernels()
    typer.echo("Available Jupyter kernels:")
    for kernel in kernels:
        typer.echo(kernel)

@app.command()
def add(name: str, display_name: str = typer.Option(None, "--display-name", "-d", help="Display name of the kernel")):
    """Add a new Jupyter kernel."""
    if display_name is None:
        display_name = name  # Use the kernel 'name' as the display name if none is provided
    kernel_manager.add_kernel(name, display_name)
    typer.echo(f"Kernel '{name}' added successfully.")


@app.command()
def remove(name: str):
    """Remove an existing Jupyter kernel."""
    kernel_manager.remove_kernel(name)
    typer.echo(f"Kernel '{name}' removed successfully.")

@app.command()
def rename(old_name: str, new_name: str):
    """Rename an existing Jupyter kernel."""
    kernel_manager.rename_kernel(old_name, new_name)
    typer.echo(f"Kernel '{old_name}' renamed to '{new_name}' successfully.")

if __name__ == "__main__":
        app()