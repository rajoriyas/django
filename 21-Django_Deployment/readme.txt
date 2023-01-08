Run following command to setup:
  Make Enviroment:
    mkvirtualenv --python=python3.8 myDjanogEnv

  Install Django:
    pip install -U django==3.0.3

  Confirmation Installation:
    which django-admin.py # should be exixts

  Place Directory:
    git clone https://github.com/rajoriyas/django-deployment-example.git

  Change Directory:
    cd django-deployment-example/
    cd first_project_with_password/

  Apply Migration:
    python manage.py
    python manage.py makemigrations
    python manage.py

  Create Super User
    python manage.py createsuperuser

  Dependencies:
    # python -m pip install argon2
    # pip install django[argon2]
    python -m pip install argon2_cffi   # use this to avoid low_level error
    # may be more according to demand

Don't forget to do this:
  # In first_project_with_password/settings.py File
    DEBUG = False
    ALLOWED_HOSTS = ['rajoriyas.pythonanywhere.com', 'http://rajoriyas.pythonanywhere.com']


Add following path to Static Files in Web Apps:
  Virtual Enviroment:
    /home/rajoriyas/.virtualenvs/myDjanogEnv

  Static Files
  URL                   Directory
  /static/admin         /home/rajoriyas/.virtualenvs/myDjanogEnv/lib/python3.8/site-packages/django/contrib/admin/static/admin/
  /static/              /home/rajoriyas/django-deployment-example/first_project_with_password/static
