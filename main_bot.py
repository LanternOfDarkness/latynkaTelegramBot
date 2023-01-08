import telebot
import latynka
import traceback
import os


with open('token.txt', 'r') as f:
    TOKEN = f.read()
    
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text', 'photo', 'video'])
def get_text_messages(message):
    CHAT_ID = message.chat.id
    if message.text == "/start":
        bot.send_message(CHAT_ID, "Привіт. Цей бот дозволяє перекласти український текст з кирилиці на латинку. \n Детальніше можете дізнатись за посиланням: \n https://www.youtube.com/watch?v=nHeE2x2UNw4")
        bot.send_message(CHAT_ID, "Знайшли помилку? Пишіть: @SBU_agent_142")
        bot.send_message(CHAT_ID, "Пришли повідомлення українською щоб перевести його в латинку.")

    else:
        try:
            lat = latynka.replace_forward(message.text)
            bot.send_message(CHAT_ID, lat)
        except Exception:
            traceback.print_exc()

print("bot_launched")
bot.polling(none_stop=True, interval=0)
