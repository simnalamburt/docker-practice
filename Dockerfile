FROM python:3.6.0-alpine
MAINTAINER Hyeon Kim <simnalamburt@gmail.com>

# Prepare app environment
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "./main.py" ]
