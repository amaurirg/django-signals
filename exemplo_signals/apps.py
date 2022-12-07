from django.apps import AppConfig


class ExemploSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exemplo_signals'


    def ready(self):
        import exemplo_signals.signals
