# State-Server (VistarMedia)

Vistar serves up a mound of geospatial data both internally and to third
parties. What we need is a server to tell us which state, if any, a point is in.
Some simplified geometries are included in states.json (so greatly simplified,
that some of the smaller ones disappear).

It need not be fast, but the code should be readable, and the results should be
correct.

## Expected Behavior

$ ./state-server &
[1] 21507
$ curl  -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/
["Pennsylvania"]

## Implementation

The above requirement has been built using `Flask` which is a microframework
for `Python`. The application has been containerised using `Docker` for the ease of use.
Container runs on `localhost` with port number `5000`.

The available `make` targets are as follows:

### `make clean`

Cleans the project by killing dangling images, containers etc in the system. This is done to ensure that no local application
is running on the port `5000`.

### `make build`

Builds the Docker image named as `state-server`.

### `make run`

Spins up the container built from image `state-server` which runs on `localhots` and 
port `5000`.

## How to run the application

### 1 - Via `Docker`
(Assumes that [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) are installed in your machine)

Go to `terminal` and run following commands.
* `git clone git@github.com:Parushgit/State-Server.git`
* `cd` to directory `State-Server`
* Run `make clean`
* Run `make build`
* Run `make run`
* Open a new `terminal` window and run `curl -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/`


### 2 - Via manually
(Assumes that [flask](http://flask.pocoo.org/docs/1.0/installation/) and [python](https://www.python.org/downloads/) is installed in your machine)

Go to `terminal` and run following commands.
* `git clone git@github.com:Parushgit/State-Server.git`
* `cd` to directory `State-Server`
* Run `FLASK_APP=server.py flask run`
* Open a new `terminal` window and run `curl -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/`

Expected output:

![Output1](https://github.com/Parushgit/State-Server/blob/master/screenshots/Docker.png)
![Output2](https://github.com/Parushgit/State-Server/blob/master/screenshots/Output.png)


## Docker image