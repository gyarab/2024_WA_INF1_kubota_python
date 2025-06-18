from django.apps import AppConfig

class LeonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leon_app'

    def ready(self):
        import leon_app.signals