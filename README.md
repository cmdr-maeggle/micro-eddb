# micro-eddb
A small web application for Elite Dangerous players (wip)

## Setup

Install Python and Django:

    python -m pip install django==1.9.3

Create a secret-key.txt (content may be random, e.g. <http://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys>)

    cat "1234567890" > "src/EliteDangerousDatabase/secret-key.txt"

## Run Application

Run the test server:

    cd src
    python EliteDangerousDatabase/manage.py runserver 8000
    
