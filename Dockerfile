FROM python:3.12.2-alpine3.19

EXPOSE 5000

WORKDIR /app

RUN apk add git 

ADD requirements.txt .

RUN pip3 install -r requirements.txt

COPY wsgi.py .
COPY config.py .
COPY application application


CMD [ "python3", "wsgi.py" ]