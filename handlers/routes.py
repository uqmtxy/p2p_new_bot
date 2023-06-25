from flask import request, abort, Response
from modules import modules
import telebot
import time
import os


def configure_routes(app, bot):
    @app.route("/" + str(os.getenv("SECRET")), methods=["POST"])
    def index():
        bot.remove_webhook()
        time.sleep(1)
        bot.set_webhook(url=os.getenv("URL"))
        
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return "ok", 200

    # @app.route('/webhook', methods=['POST'])
    # def webhook():
    #     update = telebot.types.Update.de_json(
    #         request.stream.read().decode("utf-8"))
    #     bot.process_new_updates([update])
    #     return "ok", 200
