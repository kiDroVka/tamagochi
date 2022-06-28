from PIL import Image
import random
from io import BytesIO
from bot import *
from static import *
users = {}

class Game:
    def __init__(self, id):
        self.id = id
        self.img = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{random.randint(100,900)}.png"
        self.food = 7
        self.clean = 3
        self.mood = 5
        self.sleep = 5
        self.score = 0
        bot.send_photo(self.id,self.img,"УРА, посмотри на своего нового тамагочи!")
        users.update({id: self})

    def send_photo(self,caption):
        bot.send_photo(self.id, self.img, caption=caption)

    def eat(self):
        self.food+=1
        print(self.food)
        if self.food > 5:
            bot.send_message(self.id,"Ням ням")
        else:
            bot.send_message(self.id, "Я все еще голоден!")

    def wash(self,message):
        self.clean = 3
        with open(dict_menu_buttons[message.text], 'rb') as audio:
            bot.send_voice(message.chat.id, audio)
        bot.send_message(self.id, "Ура, я чистый!")

    def sleep(self, message):
        with open("колыб.mp3", 'rb') as audio:
            bot.send_voice(message.chat.id, audio)
        bot.send_message(self.id, "Как я хорошо поспал...спасибо)")

    def status(self):
        self.send_photo(f"Сытость {self.food}/7\nЧистота {self.clean}/3\nНастроение {mood[self.mood]}\nСон {self.sleep}/5\nВаш счет {self.score}")

    def check(self):
        attr_list = ("food", "sleep", "clean")
        self.score += 1
        self.mood = sum([getattr(self, attr) for attr in attr_list])//3
        for attr in attr_list:
            print(self.mood)
            setattr(self, attr, getattr(self, attr) - 1)
            try:
                bot.send_message(self.id,globals()[attr][getattr(self, attr)])
            except:
                pass
        if self.food <= 0:
            bot.send_message(self.id,"Ваш тамагочи...умер.Но вы можете взять нового через /start ))")
            users[self.id] = ""