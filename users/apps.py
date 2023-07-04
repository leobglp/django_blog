from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #Setting up the signals
        import users.signals
