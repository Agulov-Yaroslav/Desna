import telebot
from responses import roll, prediction, game_name, swear_words_antwort

from processing import preprocess_input

API_TOKEN = '7853274476:AAEZk8nbMTaPCbsXPl4tXxgiEGPbvFogFPw'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)  # Обработка всех сообщений
def check_message(message):
    mess_low = message.text.lower()
    processed_words = preprocess_input(mess_low)

    g_name = game_name(message.from_user.username)

    print(processed_words)

    throw_dice = ['бросить', 'сделать', 'бросок', 'кинуть', 'кубик']
    make_prediction = ['судьба', 'будущее', 'удача', 'путь', 'звезда', 'сон', 'мечта', 'пророчество']
    swear_words = ['сука', 'блядь', 'хуй', 'сук', 'пизда', ]
    appeal_god = ['десна', 'богиня']

    if any(word in processed_words for word in appeal_god):
        bot.send_message(message.chat.id, 'Я тут, Если хочешь знать свою судьбу Спроси меня звёздах')
    elif any(word in processed_words for word in throw_dice):
        bot.send_message(message.chat.id, roll())
    elif any(word in processed_words for word in make_prediction):
        mess = prediction()
        bot.send_message(message.chat.id, mess)
    elif any(word in processed_words for word in swear_words):
        bot.reply_to(message, f'{g_name}! {swear_words_antwort()}')


bot.infinity_polling()
