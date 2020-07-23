from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ts0571g48v2bI+p+O5nbTxw5S6ti5/Pd5lbflajbXL0y7hHPBJ6l+TbezuDPNHhdHnCKbkFRt7Xva9paotmTkwv2GX7R2TJ+xiE952U2I6DBksbeHowTIx+slyIPmN9+BmDkra69BV38oJ4114xH3AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('87458c5b703a5a307e39f989f0c06108')

# 增加的這段放在下面
from flask import render_template
@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")
# 增加的這段放在上面

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        # Phoebe 愛唱歌
        pretty_note = '♫♪♬'
        pretty_text = ''
        
        for i in event.message.text:
        
            pretty_text += i
            pretty_text += random.choice(pretty_note)
    
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=pretty_text)
        )
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
