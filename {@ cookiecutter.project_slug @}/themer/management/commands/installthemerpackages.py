import subprocess
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from themer.lib import get_themer_path

class Command(BaseCommand):
    help = "This script installs the node_modules for the themer app."

    def handle(self, *args, **kwargs):
        themer_path = Path(get_themer_path())

        try:
            process = subprocess.Popen(
                ['npm', 'install'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=themer_path,
                shell=True
            )
            for line in process.stdout:
                self.stdout.write(line)
            process.wait()

            # Check if there were any errors during the execution
            if process.returncode != 0:
                error_output = process.stderr.read()
                if error_output:
                    self.stderr.write(f"Error during npm install: {error_output}")
                else:
                    self.stderr.write("Error during npm install: Unknown error occurred.")
            else:
                self.stdout.write(self.style.SUCCESS("NPM install completed successfully!"))

        except Exception as e:
            self.stderr.write(f"An exception occurred: {str(e)}")