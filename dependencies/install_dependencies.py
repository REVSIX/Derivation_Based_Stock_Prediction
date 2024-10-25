import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All required packages have been successfully installed.")
    except subprocess.CalledProcessError:
        print("An error occurred while installing the required packages.")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()