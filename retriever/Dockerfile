FROM python:3.6.5-alpine

WORKDIR /app
COPY ./app.py /app

RUN pip install tweepy
RUN pip install redis

EXPOSE 57369:57369

CMD [ "python", "/app/app.py" ]
