# Readme

## Create and activate virtual environment

    python3 -m venv venv
    source venv/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Run docker container of postgresql

    docker run -d --name some-postgres -e POSTGRES_PASSWORD=mySecretPassword -e POSTGRES_USER=myUser -e POSTGRES_DB=myDB -p 5432:5432 postgres

## Run the api

    uvicorn app.main:app --reload
