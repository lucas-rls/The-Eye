# Description
This project uses Django along with Postgresql to store event sent by websites to keep track of user's behaviors. As it should receive so many events at the same time, it implements Celery along with Redis to treat those requests asynchronously. To restrict access and just consider the own websites as trusted clients, the ALLOWED_HOSTS in django settings should be changed.

# Requirements to run
- [Docker]("https://docs.docker.com/engine/install/") 
- [Docker Compose]("https://docs.docker.com/compose/install/")

# How to run
To run this project, type the docker compose build
```docker
docker-compose up --build
 ```

At this moment, 4 containers will be running: 
- the_eye_celery
- the_eye_the_eye
- postgres:10-alpine
- redis:alpine

In order to access the admin panel, it's necessary to create a superuser. To do this, check the container id from  the_eye_the_eye container with the command "docker ps" and run:
```bash
docker exec -it [CONTAINER_ID] python manage.py createsuperuser
```

# Endpoints
- [POST] http://localhost:8000/collector
- Used to send a event
- - session_id: string
- - category: string
- - name: string
- - data: JSON
- - timestamp: string

- [GET] http://localhost:8000/admin
- To access admin panel and manipulate the database. Use the superuser created with the command above to access.

# How to run tests
To run the 9 tests implemented for this app, check the container id from  the_eye_the_eye container with the command "docker ps" and run:
```bash
docker exec -it [CONTAINER_ID] python manage.py test
```

*To run the project without docker it'll be necessary to have redis, celery and postegresql instances running in the machine and to adapt those services configurations on settings file.*

# Models
- <b>Category</b> - As this project should be a centralized application to capture events from different websites, I thought it should make sense to control categories from The Eye, for the frontend applications to respect a pattern.
- <b>Event</b> - The Event model, with all the params received in the POST endpoint above in addition with a created_at column to store de timestamp at the moment it was stored.
- <b>EventError</b> - The EventError model is used to store the events that couldn't be stored because of some error. This should help to keep track of possibles frontend errors or some violations.

# Website
I created two simple templates to simulate the real event generator action. You can access on "http://localhost:8000/website/". The events that can be generated are:
- Page View - Triggered when a page is accessed.
- - "category": "page interaction"
- - "name": "pageview"
- Image Click - Triggered when the home image is clicked.
- - "category": "page interaction"
- - "name": "banner image click"
- Form Submit - Triggered when the form is submitted.
- - "category": "form interaction"
- - "name": "submit"
- - "data" key has carries the form information