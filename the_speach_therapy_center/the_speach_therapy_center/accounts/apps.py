from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'the_speach_therapy_center.accounts'

    def ready(self):
        import the_speach_therapy_center.accounts.signals
