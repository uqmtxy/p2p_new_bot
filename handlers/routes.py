from flask import request, abort, Response
from modules import modules
import telebot
import time
import os


def configure_routes(app, bot):
    @app.route("/", methods = ['POST', 'GET'])
    def index():
        # bot.remove_webhook()
        # time.sleep(1)
        # bot.set_webhook(url=os.getenv("URL"))
        if request.headers.get('content-type')=='application/json':
            update = telebot.types.Update.de_json(
                request.stream.read().decode("utf-8"))
            bot.process_new_updates([update])
            return "I'm alive"
        else: 
            abort(403)
        if request.method == 'POST':
            return Response('ok', status=200)
        else:
            return ""

    # @app.route('/webhook', methods=['POST'])
    # def webhook():
    #     update = telebot.types.Update.de_json(
    #         request.stream.read().decode("utf-8"))
    #     bot.process_new_updates([update])
    #     return "ok", 200
