from flask import request, abort, Response
from modules import modules
import asyncio
import telebot
import time
import os


def configure_routes(app, bot):
    
    @app.route("/")
    def index():
        bot.remove_webhook()
        bot.set_webhook(url=os.getenv("URL"))
        return "I'm alive"
    
    @app.route("/" + str(os.getenv("SECRET")), methods=["POST"])
    def webhook():    
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return "ok", 200
