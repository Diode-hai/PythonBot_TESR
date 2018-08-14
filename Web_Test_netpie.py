from flask import Flask, request, abort

import requests # pip install requests
import urllib3

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#Token
line_bot_api = LineBotApi('uPPbuNIIATryuuhKwEC4kRRHqdNd4+73PnMi+7DQ383G4NMkI6S7a+li5SCoqZJGbKsl3sxQ6J556VApXNkprhB4dKVg1rR6UcHZzSTFyte5h0qyqFAb9zISLsL5LEw+DS/KlnXV/IG5UDYV3g6qjQdB04t89/1O/w1cDnyilFU=')
#Channel secret
handler = WebhookHandler('bce117e84ff9f7e593d428b1ffac7aa4')

APPID="BotChatLine"
KEY = "me37I8KsiCqpTWS"
SECRET = "ozPtNGTK6GPA1STe1PjIvvrwS"
Topic = "/LED_Control"
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()

#-------------------------------------------------

