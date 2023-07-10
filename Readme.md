# Solar Panel Electricity Price Downloader App

This Django project allows you to download electricity prices for solar panels from a specific URL, store the data in a PostgreSQL database, and render it. It consists of three Docker containers, one for the app, one for the PostgresSQL database and one for the message broker(RabbitMQ).

## Installation

Before cloning the project, make sure that you have installed Docker on your system. If you don't have it you can download it from the official website:

https://www.docker.com/products/docker-desktop/

1. Clone the repository to your local machine:
    - "git clone git@github.com:ivaylobandrov/DjangoAdvancedProjectITIDO.git"

2. Don't forget to update the .env file with desired data. You can remove the .example from the .env.example file and update it with the actual information.

3. Once cloned to your local machine you can start the project with the following command:
   - "docker-compose up --build"

   - Note that the flag "--build" is required only the first time, after that you can start the project without it.

4. Have fun!