# Project setup

The [pipenv](https://docs.pipenv.org) tool is using as a 
dependencies management tool

```bash
pipenv shell
python manage.py runserver
```

# Other



## Project commands

```bash
# activate the virtual environment
pipenv shell

#install deps
pipenv sync --dev

#install dev deps
pipenv sync --dev

#install new dependency
pipenv install requests
pipenv install --dev httpx

#lock dependencies. Update the Pipfile.lock
pipenv lock
```