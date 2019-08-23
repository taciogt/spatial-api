FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -qq binutils=2.31.1-16 libproj-dev=5.2.0-1 gdal-bin=2.4.0+dfsg-1+b1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend /code/
#ADD ./run_local_server.sh /code/