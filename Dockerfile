FROM --platform=linux/x86_64 python:3.11.6-slim

ENV PYTHONPATH=src/

# Update the system and install packages
RUN apt-get update -y \
    && pip install --upgrade pip \
    # dependencies for building Python dependencies
    && pip install --upgrade setuptools \
    && apt-get install -y build-essential \
    && pip install pipenv \
    # cleaning up unused files
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY ./Pipfile ./Pipfile.lock /
RUN pipenv sync --dev --system 


WORKDIR /app/
COPY ./ ./

ENTRYPOINT [ "gunicorn" ]
CMD ["--workers=2", "config.wsgi:application", "--bind=0.0.0.0:8000" ]

# Another variant:
# CMD python src/manage.py runserver 0.0.0.0:8000