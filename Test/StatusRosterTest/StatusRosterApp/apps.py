from django.apps import AppConfig


class StatusrosterappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StatusRosterApp'

    def ready(self):
        import StatusRosterApp.signals