import os
import json
from shutil import rmtree, move
from jupyter_core.paths import jupyter_data_dir
from ipykernel.kernelspec import make_ipkernel_cmd, write_kernel_spec

class KernelManager:
    def __init__(self):
        self.kernel_dir = os.path.join(jupyter_data_dir(), 'kernels')

    def _kernel_path(self, name):
        return os.path.join(self.kernel_dir, name)
    
    def _ensure_kernel_dir_exists(self):
        if not os.path.exists(self.kernel_dir):
            os.makedirs(self.kernel_dir, exist_ok=True)
            
    def list_kernels(self):
        """List all available Jupyter kernels."""
        if os.path.exists(self.kernel_dir) and os.path.isdir(self.kernel_dir):
            return next(os.walk(self.kernel_dir))[1]
        else:
            print("Kernel directory does not exist or is not a directory.")
            return []
        
    def add_kernel(self, name, display_name, **kwargs):
        """Add a new Jupyter kernel."""
        kernel_cmd = make_ipkernel_cmd(mod='ipykernel_launcher', **kwargs)
        path = write_kernel_spec(overrides={'argv': kernel_cmd, 'display_name': display_name})

        # Move the kernel spec to the Jupyter kernels directory
        dest_path = self._kernel_path(name)
        if os.path.exists(dest_path):
            rmtree(dest_path)
        move(path, dest_path)

    def remove_kernel(self, name):
        """Remove an existing Jupyter kernel."""
        kernel_path = self._kernel_path(name)
        if os.path.isdir(kernel_path):
            rmtree(kernel_path)

    def rename_kernel(self, old_name, new_name):
        """Rename an existing Jupyter kernel."""
        old_path = self._kernel_path(old_name)
        new_path = self._kernel_path(new_name)
        if os.path.isdir(old_path):
            move(old_path, new_path)
