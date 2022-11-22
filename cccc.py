import telebot
import string
import random
#ascii _lowercase


bot = telebot.TeleBot("5501084502:AAFqx5l63-weNkzOlobhF1wXLvp1Z-mXCkg")
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"<b>Бот является пробной версией</b>", parse_mode="html")
    elif 'Пароль' in message.text:
        baza = string.ascii_letters + string.digits
        password = "".join(random.choice(baza)for i in range(15))
        bot.send_message(message.chat.id, f"ВАШ ПАРОЛЬ: {password}")
    else:
        bot.send_message(message.from_user.id, "ЧТО ТЫ НЕСЕШЬ?")
        bot.send_message(message.from_user.id, "Команды:")
        bot.send_message(message.from_user.id, "Привет")    
        bot.send_message(message.from_user.id, "Генератор пароля")



bot.polling()
