from flask import request, abort, Response
from modules import modules
import telebot
import time
import os


def configure_routes(app, bot):
    
    @app.route("/")
    async def index():
        await bot.remove_webhook()
        await time.sleep(1)
        await bot.set_webhook(url=os.getenv("URL"))
        return "I'm alive"
    
    @app.route("/" + str(os.getenv("SECRET")), methods=["POST"])
    async def webhook():    
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        await bot.process_new_updates([update])
        return "ok", 200
