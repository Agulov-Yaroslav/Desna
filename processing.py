from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
import pymorphy2

stop_words = set(stopwords.words('russian'))  # Загружаем русские стоп-слова
morph = pymorphy2.MorphAnalyzer()


def preprocess_input(user_input):
    tokens = word_tokenize(user_input, language='russian')
    processed_words = []
    for word in tokens:
        # Если это слово состоит только из букв/цифр и не является стоп-словом
        if word.isalnum() and word not in stop_words:
            lemma = morph.parse(word)[0].normal_form  # Применяем лемматизацию
            processed_words.append(lemma)

    bigrams = list(ngrams(processed_words, 2))
    return processed_words
