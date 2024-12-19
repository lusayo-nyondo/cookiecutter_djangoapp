import os
import shutil
from django.core.management import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "Clear all __pycache__ from the project directory, ignoring venv."

    def handle(self, *args, **options):
        BASE_PATH = getattr(settings, 'BASE_DIR')

        for root, dirs, files in os.walk(BASE_PATH):
            if 'venv' in root:
                continue 
            
            if 'migrations' in dirs:
                pycache_path = os.path.join(root, 'migrations')
                print(f"Removing: {pycache_path}")
                shutil.rmtree(pycache_path)
