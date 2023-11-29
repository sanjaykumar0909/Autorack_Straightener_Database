from django.apps import AppConfig
from django.core import management as mgmt
import threading

class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    def ready(self):
        def run():
            mgmt.call_command("push_data")

        thread = threading.Thread(target=run, daemon= True)
        thread.start()