import json
from flask import Flask, request
import slack
import os
from slackeventsapi import SlackEventAdapter
import pymongo
import logging

#VERSION WINDOWS

'''from pathlib import Path
from dotenv import load_dotenv
path = Path('.') / '.env'
load_dotenv(dotenv_path=path)
TOKEN = os.environ["SLACK_TOKEN"]
SIGNING_SECRET = os.environ["SIGNING_SECRET"]
'''

#VERSION UNIX
TOKEN = os.environ.get("SLACK_TOKEN")
SIGNING_SECRET = os.environ.get("SIGNING_SECRET")

#OBTENER DEL NAVEGADOR:
#                       IR A ESPACIO DE TRABAJO Y SELECCIONAR CANAL
#                       EL CHANNEL ID SERA LA ULTIMA SERIE DE DIGITOS-LETRAS ESE LINK
#                       https://app.slack.com/client/XXXXXXXXXXX/C01CB597ZA6

client = slack.WebClient(token=TOKEN)
mongo_client = pymongo.MongoClient(os.environ.get('MONGO_HOST'), int(os.environ.get('MONGO_PORT')))
db = mongo_client['bot']
collection = db['mensajes']


app = Flask(__name__)

slack_event = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)

BOT_ID = client.api_call('auth.test')['user_id']


#Obtener ID's y nombre de usuarios
result_users = client.users_list()['members']
users = {}

for user in result_users:
    users[user['id']] = user['name']

result_channels = client.conversations_list()['channels']
channels = {}

for channel in result_channels:
    channels[channel['id']] = channel['name']

@app.route("/")
def hello():
    return "Qué tal!"

@slack_event.on('message')
def message(payload):

    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    # 1) “OK Néstor, cuál es el último mensaje enviado por [“nombre de usuario del canal”]
    # 2) “OK Néstor, cuántos mensajes han sidos enviados por [“nombre de usuario del canal”]

    if user_id != BOT_ID:

        user_name = text.split(' ')[-1]
        print(channels[channel_id])
        if text.rstrip(user_name).lower() == 'ok nestor, cual es el ultimo mensaje enviado por ':
            
            query = collection.find({'channel': channels[channel_id], "user": user_name}).sort("_id", pymongo.DESCENDING).limit(1)
                        
            cont=0
            for i in query:
                cont+=1
                client.chat_postMessage(channel=channel_id, text='El ultimo mensaje enviado por @' + user_name + 'es: ' + i['text'])

            if cont == 0:
                client.chat_postMessage(channel=channel_id, text='El usuario @' + user_name + ' no ha enviado mensajes.')


        elif text.rstrip(user_name).lower() == 'ok nestor, cuantos mensajes han sidos enviados por ':
            query = collection.find({'channel': channels[channel_id], "user": user_name}).count()
            client.chat_postMessage(channel=channel_id, 
                                    text='El usuario @' + user_name + ' ha enviado' + str(query) + 
                                         ' mesajes')

        else:
            collection.insert_one(
                {'channel': channels[channel_id],'user': users[user_id], 
                "text": text}
            )



if __name__ == '__main__':
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000)