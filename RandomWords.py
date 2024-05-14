from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if word_dict is None:
            continue

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        translate_word_definition = translator.translate(word_definition, dest="ru")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        print(f"Перевод значения слова - {translate_word_definition.text}")
        user = input("Что это за слово? ")

        # Переводим ответ игрока на английский
        translated_user_answer = translator.translate(user, dest="en").text.lower()

        if translated_user_answer == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")
            translate_word = translator.translate(word, dest="ru")
            print(f"Перевод загаданного слова - {translate_word.text}")

        # Создаём возможность закончить игру

        play_again = input("Хотите сыграть еще раз? y/n\n")


        if play_again.lower != "y":
            print("Спасибо за игру!")
            break


word_game()