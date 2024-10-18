import nltk
import telebot
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import random


API_TOKEN = '7853274476:AAEZk8nbMTaPCbsXPl4tXxgiEGPbvFogFPw'

bot = telebot.TeleBot(API_TOKEN)
 # Вместо Lemm
stop_words = set(stopwords.words('russian')) # Загружаем русские стоп-слова

def preprocess_input(user_input):
    tokens = word_tokenize(user_input)
    processed_words = []
    for word in tokens:
        # Если это слово состоит только из букв/цифр и не является стоп-словом
        if word.isalnum() and word not in stop_words:
            # Приводим слово к его базовой форме (лемматизация) и добавляем в список
            lemmword = morph.parse(word)[0].normal_form
            print(lemmword)
            processed_words.append(lemmword)

    return processed_words

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Богиня благословляет этот прекрасный мир')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Бог поможет')


@bot.message_handler(func=lambda message: True)  # Обработка всех сообщений
def check_message(message):
    mess_low = message.text.lower()
    afer_proc_words = preprocess_input(mess_low)
    print(afer_proc_words)

    keyword_pattern = r'\bдесна\b|\bдесны\b|\bдесне\b|\bдесну\b|\bдесной\b|\bдесной\b'
    if re.search(keyword_pattern, message.text.lower()):
        bot.send_message(message.chat.id, 'Я тут')


bot.infinity_polling()

