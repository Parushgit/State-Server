# Docker Configurations
COMPOSE_FILE:=docker-compose.yml
CONTAINER_NAME:=state-server
DOCKER_FILE:=Dockerfile

.PHONY: clean
clean:
	docker-compose -f $(COMPOSE_FILE) stop
	docker-compose -f $(COMPOSE_FILE) rm -f
	-docker rm --force $(CONTAINER_NAME)
	-docker images -q -f "dangling=true" | xargs -I {} docker rmi -f {}
	-docker volume ls -q -f "dangling=true" | xargs -I {} docker volume rm {}

.PHONY: build
build:
	docker build -t $(CONTAINER_NAME) -f $(DOCKER_FILE) .

.PHONY: run
run: clean build
	docker-compose -f $(COMPOSE_FILE) up