FROM python:3.12.2-alpine3.19

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD [ "python3", "main.py" ]