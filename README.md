# Automsg
This repository is dedicated to the development of an API for automating message delivery at specific times (date and time) or through repeated scheduling options (daily or at specific times on the week) for both WhatsApp and Discord platforms.


# Start the Docker container

    $ cd automsg
    $ docker-compose up --build
# Delete the container
#### If these containers are currently running, stop them first:

    $ docker stop my-django-container my-react-container my-mysql-container

#### And then remove them:

    $ docker rm my-django-container my-react-container my-mysql-container
