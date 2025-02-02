FROM python:3.10.7-slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y gcc libc-dev make git libffi-dev python3-dev libxml2-dev libxslt-dev

RUN apt-get install -y default-libmysqlclient-dev

RUN apt-get install -y libpq-dev

RUN pip install -U pip

RUN pip install harambot

EXPOSE  10000

CMD ["harambot"]
