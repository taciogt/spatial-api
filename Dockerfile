FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -qq binutils libproj-dev gdal-bin

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend /code/
#ADD ./run_local_server.sh /code/