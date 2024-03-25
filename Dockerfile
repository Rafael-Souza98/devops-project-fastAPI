FROM python:3.12.2-alpine3.19

EXPOSE 5000

WORKDIR /app

RUN apk add git 

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY main.py .

CMD [ "python3", "app.py" ]