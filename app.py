import telebot
import os
import openai
import time
import requests
import random
from telebot import types
from flask import Flask
from modules import modules
from handlers.routes import configure_routes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")


bot = telebot.TeleBot(token=TOKEN, threaded=False)
app = Flask(__name__)


configure_routes(app, bot)



@bot.message_handler(commands=["start"])
def start_message(message):
    mess = f"""
            Здравствуйте, {message.from_user.first_name}!   
Я - бот для торговли на P2P. Чего бы Вы хотели сегодня?
            """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_text = "/get_rates "
    # button_action = types.KeyboardButton(button_text, callback_data="/get_rates")
    button_action = types.KeyboardButton(button_text)
    markup.add(button_action)
    bot.send_message(
        message.chat.id, mess, reply_markup=markup, parse_mode="html"
    )
    # await bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["get_rates"])
def get_all_rates(message):
    currency = modules.BinanceCurrency()
    mess = ""
    for this_currency_info in currency.get_default_params().values():
        # print(this_currency_info)
        currency.set_params_custom(this_currency_info)
        for bank in this_currency_info["payTypes"]:
            currency.set_params_fiat_pay_types(
                _fiat=currency.get_param_fiat(), _pay_types=[bank]
            )
            mess += f"""
{currency.get_param_pay_types()[0]} $USD = {currency.compute_rates()} {currency.get_param_fiat()}
            """
    bot.send_message(message.chat.id, mess, parse_mode="html")


# if __name__ == "__main__":
#     app.run(debug=True)
