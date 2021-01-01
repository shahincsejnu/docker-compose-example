# Docker Compose Example by making a client-server using python, HTML, Dockerfile

## followed tutorial is [here](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa/)


## Build docker-compose

- `docker-compose build`

## Run docker-compose

- `docker-compose up`


## useful commands for docker-compose

### stops container and remove containers, images...created by 'docker-compose up'

- `docker-compose down`

### Diplays log output from services

- `docker-compose logs -f <service_name>`

### Lists containers

- `docker-compose ps`

### Executes a command in a running container

- `docker-compose exec <service_name> <command>`

### Lists images

- `docker-compose images`