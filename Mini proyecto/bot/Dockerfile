FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="WRITE HERE YOUR SLACK TOKEN"
ENV SIGNING_SECRET="WRITE HERE YOUR SLACK SIGNING_SECRET"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /bot

COPY ./proyecto.py /proyecto.py

CMD [ "python", "/proyecto.py" ]
