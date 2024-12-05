import os
import subprocess
import sys

def create_virtualenv(venv_path):
    """Create a virtual environment."""
    subprocess.check_call([sys.executable, '-m', 'venv', venv_path])

def activate_virtualenv(venv_path):
    """Return the activation command for the virtual environment."""
    if os.name == 'nt':  # Windows
        return os.path.join(venv_path, 'Scripts', 'activate.bat')
    else:  # Unix or MacOS
        return os.path.join(venv_path, 'bin', 'activate')

def install_requirements(venv_path):
    """Install requirements from requirements.txt."""
    pip_executable = os.path.join(venv_path, 'Scripts' if os.name == 'nt' else 'bin', 'pip')
    
    requirements_file = os.path.join(os.getcwd(), 'requirements', 'base.txt')
    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])
    
    requirements_file = os.path.join(os.getcwd(), 'requirements', 'base_experimental.txt')
    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])

def run_management_commands(venv_path):
    """Run Django management commands."""
    python_executable = os.path.join(venv_path, 'Scripts' if os.name == 'nt' else 'bin', 'python')
    
    print("Making and running migrations...")
    subprocess.check_call([python_executable, 'manage.py', 'makemigrations'])
    subprocess.check_call([python_executable, 'manage.py', 'migrate'])
    
    print("Setting up themer...")
    subprocess.check_call([python_executable, 'manage.py', 'installthemerpackages'])
    subprocess.check_call([python_executable, 'manage.py', 'collectcolors'])
    
if __name__ == "__main__":
    venv_path = os.path.join(os.getcwd(), 'venv')

    print(f"Creating venv at: { venv_path }")
    create_virtualenv(venv_path)
    
    print(f"Installing requirements in venv")
    install_requirements(venv_path)
    
    print("Run management commands")
    run_management_commands(venv_path)

    print("Setup completed successfully!")