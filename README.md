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
Container runs on `localhost` with port number `8080`.

The available `make` targets are as follows:

### `make clean`

Cleans the project by killing dangling images, containers etc in the system. This is done to ensure that no local application
is running on the port `8080`.

### `make build`

Builds the Docker image named as `state-server`.

### `make run`

Spins up the container built from image `state-server` which runs on `localhost` and 
port `8080`.

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
(Assumes that [flask](http://flask.pocoo.org/docs/1.0/installation/) and [python](https://www.python.org/downloads/) are installed in your machine)

Go to `terminal` and run following commands.
* `git clone git@github.com:Parushgit/State-Server.git`
* `cd` to directory `State-Server`
* Run `python server.py`
* Open a new `terminal` window and run `curl -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/`

Expected output:

![Output1](https://github.com/Parushgit/State-Server/blob/master/screenshots/Docker.png)
![Output2](https://github.com/Parushgit/State-Server/blob/master/screenshots/Output.png)


## Testing
Please find below some of the test cases:
* curl -d "longitude=-111.216141&latitude=34.666038" http://localhost:8080/
["Arizona"]
* curl -d "longitude=-99.967462&latitude=32.839522" http://localhost:8080
["Texas"]
* curl -d "longitude=-104.5691185&lati" http://localhost:8080/
Input is not correct. Please curl it again!
* curl -d "longitude=-75.7907503&latitude=49.0945688" http://localhost:8080/
Given coordinates are outside of United States. Try again!


## Docker image

[Docker Hub Link](https://hub.docker.com/r/parushgarg/vistarmedia/)

`docker pull parushgarg/vistarmedia`. This will greatly help if the application needs to be scaled up or down via `Kubernetes` on any cloud platform.



