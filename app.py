from flask import Flask, request, jsonify
from constants import TOKEN
from pymessenger.bot import Bot
import util

app = Flask(__name__)
bot = Bot(TOKEN)

@app.route('/webhook', methods = ['GET'])
def get_webhook():
    if request.args.get('hub.verify_token') == TOKEN:
        return request.args.get('hub.challenge')
    return "Wrong Verify Token"

@app.route('/webhook', methods = ['POST'])
def post_webhook():
    recipentId = util.get_senderId(request.json)
    message = util.get_message(request.json)
    bot.send_text_message(recipentId, message)
    return jsonify({"response" : "sucess"})



if __name__ == '__main__':
    app.run(port = 8000, debug=True)