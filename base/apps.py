"""
Create your own AppConfig class like described below

from django.apps import AppConfig

class <APPNAME>Config(AppConfig):
    name = '<APPNAME>'
    verbose_name = '<Humnaized Appname>'


    def ready(self):
        # Import all the signals defined in your application
        import 'project.app.signals'
"""
