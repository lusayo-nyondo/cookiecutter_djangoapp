import os, shutil
from django.core.management import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "Clear all pycache from the project directory."
    
    def handle(self, *args, **options):
        BASE_PATH = getattr(settings, 'BASE_DIR')
        
        for root, dirs, files in os.walk(BASE_PATH):
            if '__pycache__' in dirs:
                pycache_path = os.path.join(root, '__pycache__')
                print(f"Removing: {pycache_path}")  # Optional: print the path being removed
                shutil.rmtree(pycache_path) 