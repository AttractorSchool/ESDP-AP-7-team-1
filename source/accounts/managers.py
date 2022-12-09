from django.contrib.auth.models import UserManager


class AccountManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = email if not username else username
        return super(AccountManager, self).create_superuser(username, email, password, **extra_fields)

