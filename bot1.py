import telebot
import config
import random
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>. Давай сыграем в игру 😋 я загадаю число от 1 до 3, а ты попытаешься его угадать".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def game(message):
    if message.chat.type == "private":
        if message.text == "1" and str(random.randint(1, 3)) == '1':
            bot.send_message(message.chat.id, '1')
            bot.send_message(message.chat.id, "Ты угадал 👍")
        elif message.text == "2" and str(random.randint(1, 3)) == '2':
            bot.send_message(message.chat.id, '2')
            bot.send_message(message.chat.id, "Ты угадал 👍")
        elif message.text == "3" and str(random.randint(1, 3)) == '3':
            bot.send_message(message.chat.id, '3')
            bot.send_message(message.chat.id, "Ты угадал 👍")
        else:
            bot.send_message(message.chat.id, 'Ты не угадал 😢, попробуй еще раз')




bot.polling(non_stop=True)
