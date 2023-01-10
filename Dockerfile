FROM python:3.11.1-buster

RUN apt-get install python-is-python3 -y

RUN pip3 install -r requirements.txt

WORKDIR /app
COPY . .

CMD python3 forwardgram.py config.yml