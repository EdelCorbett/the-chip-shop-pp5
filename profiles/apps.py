from django.apps import AppConfig
from django.db.models.signals import post_save


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        from profiles.signals import create_user_profile
        from django.contrib.auth.models import User
        post_save.connect(create_user_profile, sender=User)
        from profiles.signals import save_profile
        post_save.connect(save_profile, sender=User)
