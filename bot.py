import telebot
from telebot import types
from parser import get_latest_news, check_for_new_news
import threading
import time

from config import BOT_API as API


API_TOKEN = f'{API}'
bot = telebot.TeleBot(API_TOKEN)

# Список подписчиков
subscribers = set()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Вывести 3 последних новости")
    button2 = types.KeyboardButton("Вывести последнюю новость")
    button3 = types.KeyboardButton("Подписаться на рассылку")
    button4 = types.KeyboardButton("Отписаться от рассылки")
    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "Привет! Что вы хотите сделать?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Вывести 3 последних новости")
def send_latest_3_news(message):
    news = get_latest_news(3)
    if not news:
        bot.send_message(message.chat.id, "К сожалению, нет доступных новостей.")
    for n in news:
        bot.send_message(
            message.chat.id,
            f"{n['title']}\n{n['description']}\nАвтор: {n['author']}\nСсылка: {n['link']}"
        )

@bot.message_handler(func=lambda message: message.text == "Вывести последнюю новость")
def send_latest_news(message):
    news = get_latest_news(1)
    if not news:
        bot.send_message(message.chat.id, "К сожалению, нет доступных новостей.")
        return
    n = news[0]
    bot.send_message(
        message.chat.id,
        f"{n['title']}\n{n['description']}\nАвтор: {n['author']}\nСсылка: {n['link']}"
    )

@bot.message_handler(func=lambda message: message.text == "Подписаться на рассылку")
def subscribe(message):
    subscribers.add(message.chat.id)
    bot.send_message(message.chat.id, "Вы подписались на рассылку новостей.")

@bot.message_handler(func=lambda message: message.text == "Отписаться от рассылки")
def unsubscribe(message):
    subscribers.discard(message.chat.id)
    bot.send_message(message.chat.id, "Вы отписались от рассылки новостей.")

def send_news_to_subscribers(news):
    for subscriber in subscribers:
        bot.send_message(
            subscriber,
            f"{news['title']}\n{news['description']}\nАвтор: {news['author']}\nСсылка: {news['link']}"
        )

def news_checker():
    while True:
        new_news = check_for_new_news()
        if new_news:
            send_news_to_subscribers(new_news)
        time.sleep(600)  # Проверка каждые 10 минут

if __name__ == '__main__':
    # Запускаем проверку новостей в отдельном потоке
    news_thread = threading.Thread(target=news_checker)
    news_thread.start()

    bot.infinity_polling()
