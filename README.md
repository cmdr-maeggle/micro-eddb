# micro-eddb
A small web application for Elite Dangerous players (wip)

## Setup

Install Python and Django:

    python -m pip install -r "src/eddb/requirements.txt"

Create a secret-key.txt (content may be random, e.g. <http://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys>)

    cat "1234567890" > "src/EliteDangerousDatabase/secret-key.txt"


## Run Application

Prepare the test installation:

    cd src
    python EliteDangerousDatabase/manage.py migrate
    python EliteDangerousDatabase/manage.py loaddata initial_data
    python EliteDangerousDatabase/manage.py createsuperuser

Run the test server:

    cd src
    python EliteDangerousDatabase/manage.py runserver 8000
    
Open in browser:
    http://127.0.0.1:8000
    http://127.0.0.1:8000/admin
