#Note, this bot was created to respond to a friend in chat who repeats same pictures and phrases

import os
import sys
import json
import random          
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

satania = ['https://i.imgur.com/a0c99Xy.jpg',' https://i.imgur.com/CYrJCal.jpg', 'https://i.imgur.com/dbNDYcx.jpg', 
           'https://i.imgur.com/bhnECWl.jpg', 'https://i.imgur.com/gUcWy4j.jpg',
           'https://i.ytimg.com/vi/fjbxTE4bx4k/maxresdefault.jpg'
          ]
negatives = ['cannot', 'not', 'knot', 'annoyed', 'annoy', 'annoying']

count = 0



app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  sentence = data['text']

#############################################          
  if data['name'] != 'Lunar Bot':
    if "no" in sentence.lower():
      msg = "no u"
      send_message(msg)
    if "911" in data['text']:
      msg = '911'
      end_message(msg)
  if data['text'] == '!lasagna':
    num = random.randint(0,len(satania)-1)
    msg = satania[num]
    send_message(msg)
  if data['text'] == "!count":
    count += 1
    msg = count
    send_message(msg)


#########################################
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
sys.stdout.flush()
