import datetime

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Renames a Django project'

    def handle(self, *args, **kwargs):
        debug = True
        production_email_backend = ''
        production_email_host = ''
        production_email_host_user = ''
        production_email_host_password = ''
        production_email_port = ''
        development_email_backend = ''
        development_email_host = ''
        development_email_host_user = ''
        development_email_port = ''
        datetime_now = datetime.datetime.now()

        secret_key = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')

        environment = int(input(self.style.NOTICE(
            "What is your preferred environment? "
            + "\n"
            + "1. Development"
            + "\n"
            + "2. Production"
            + "\n"
        )))

        if environment == 1:
            debug = True
            development_email_backend = 'django.core.mail.backends.console.EmailBackend'
            development_email_host = 'localhost'
            development_email_host_user = 'me@example.com'
            development_email_port = 1025
        if environment == 2:
            debug = False
            production_email_backend = 'django.core.mail.backends.smtp.EmailBackend'
            production_email_host = str(
                input(self.style.NOTICE("What is your production email host? ('Ex: 200.0.103.1): ")))
            production_email_host_user = str(
                input(self.style.NOTICE("What is your production email host user? ('Ex: production_host_user): ")))
            production_email_host_password = str(
                input(self.style.NOTICE("What is your production email host password? ('Ex: 12345678): ")))
            production_email_port = str(
                input(self.style.NOTICE("What is your production email port? (default: 465): ")))
            if not production_email_port:
                production_email_port = 465

        time_zone = str(input(self.style.NOTICE("What is your preferred timezone? (default: 'UTC'): ")))
        database_name = str(input(self.style.NOTICE("What is your database name? (default: 'django_db'): ")))
        database_user_name = str(input(self.style.NOTICE("What is your database username? (default: 'postgres'): ")))
        database_password = str(input(self.style.NOTICE("What is your database password? (default: 'postgres'): ")))

        if not time_zone:
            time_zone = 'UTC'
        if not database_name:
            database_name = 'django_db'
        if not database_user_name:
            database_user_name = 'postgres'
        if not database_password:
            database_password = 'postgres'

        writable_production_environment_dict = {
            'CURR_DATETIME': datetime_now,
            'DEBUG': debug,
            'SECRET_KEY': secret_key,
            'DATABASE_NAME': database_name,
            'DATABASE_USER': database_user_name,
            'DATABASE_PASSWORD': database_password,
            'TIME_ZONE': time_zone,
            'PRODUCTION_EMAIL_BACKEND': production_email_backend,
            'PRODUCTION_EMAIL_HOST': production_email_host,
            'PRODUCTION_EMAIL_HOST_USER': production_email_host_user,
            'PRODUCTION_EMAIL_HOST_PASSWORD': production_email_host_password,
            'PRODUCTION_EMAIL_PORT': production_email_port
        }

        writable_production_environment = '''
# Developed by: Mohd. Shafikur Rahman
# Generated on: {CURR_DATETIME}  
      
DEBUG={DEBUG}
SECRET_KEY={SECRET_KEY}
TIME_ZONE={TIME_ZONE}

# DATABASE CONFIG
DATABASE_NAME={DATABASE_NAME}
DATABASE_USER={DATABASE_USER}
DATABASE_PASSWORD={DATABASE_PASSWORD}

# EMAIL CONFIG
PRODUCTION_EMAIL_BACKEND={PRODUCTION_EMAIL_BACKEND}
PRODUCTION_EMAIL_HOST={PRODUCTION_EMAIL_HOST}
PRODUCTION_EMAIL_HOST_USER={PRODUCTION_EMAIL_HOST_USER}
PRODUCTION_EMAIL_HOST_PASSWORD={PRODUCTION_EMAIL_HOST_PASSWORD}
PRODUCTION_EMAIL_PORT={PRODUCTION_EMAIL_PORT}
''' \
            .format(**writable_production_environment_dict)

        writable_development_environment_dict = {
            'CURR_DATETIME': datetime_now,
            'DEBUG': debug,
            'SECRET_KEY': secret_key,
            'DATABASE_NAME': database_name,
            'DATABASE_USER': database_user_name,
            'DATABASE_PASSWORD': database_password,
            'TIME_ZONE': time_zone,
            'DEVELOPMENT_EMAIL_BACKEND': development_email_backend,
            'DEVELOPMENT_EMAIL_HOST': development_email_host,
            'DEVELOPMENT_EMAIL_HOST_USER': development_email_host_user,
            'DEVELOPMENT_EMAIL_PORT': development_email_port
        }

        writable_development_environment = '''
# Developed by: Mohd. Shafikur Rahman
# Generated on: {CURR_DATETIME}  

DEBUG={DEBUG}
SECRET_KEY={SECRET_KEY}
TIME_ZONE={TIME_ZONE}

# DATABASE CONFIG
DATABASE_NAME={DATABASE_NAME}
DATABASE_USER={DATABASE_USER}
DATABASE_PASSWORD={DATABASE_PASSWORD}

# EMAIL CONFIG
DEVELOPMENT_EMAIL_BACKEND={DEVELOPMENT_EMAIL_BACKEND}
DEVELOPMENT_EMAIL_HOST={DEVELOPMENT_EMAIL_HOST}
DEVELOPMENT_EMAIL_HOST_USER={DEVELOPMENT_EMAIL_HOST_USER}
DEVELOPMENT_EMAIL_PORT={DEVELOPMENT_EMAIL_PORT}
''' \
            .format(**writable_development_environment_dict)

        if environment == 1:
            with open('.env', 'w') as file:
                file.write(writable_development_environment)
                file.close()
        else:
            with open('.env', 'w') as file:
                file.write(writable_production_environment)
                file.close()
