import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types
from threading import Timer
from tamagochi import *
from static import *
#from tamagochi import Sleep

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, text="Привет, я твой карманный тамогочи".format(message.from_user),
                     reply_markup=markup.add(types.KeyboardButton("Главное меню")))
    message.from_user.id = Game(message.from_user.id)
    RepeatTimer(60
                , notify).start()


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in dict_menu_buttons:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        [markup.add(types.KeyboardButton(button)) for button in dict_menu_buttons[message.text]]
        try:
            users[message.from_user.id].wash(message)
        except:
            bot.send_message(message.chat.id, text="Чем займемся?", reply_markup=markup)
    elif message.text == "Спальня":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чем займемся?", reply_markup=markup2)
    elif message.text == "Покормить":
        users[message.from_user.id].eat()
    elif message.text == "Напоить":
        bot.send_message(message.chat.id, text="хлюп-хлюп")
    elif message.text == "Состояние":
        users[message.from_user.id].status()
    else:
        bot.send_message(message.chat.id, text="м?")



class RepeatTimer(Timer):  # класс, повторяющий сообщение
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def notify():
    for user in users.keys():
        try:
            users[user].check()
        except:
            pass

bot.infinity_polling()
