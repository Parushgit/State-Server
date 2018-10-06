FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN mkdir /src

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

COPY . /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["server.py"]