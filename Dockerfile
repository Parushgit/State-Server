FROM python:3.6.5-slim

RUN mkdir /src

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

COPY . /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["server.py"]