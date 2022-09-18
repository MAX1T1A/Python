import telebot
from telebot import types
import sqlite3
from config import teken


db = sqlite3.connect("server.db", check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
	first_name TEXT,
	last_name TEXT
)""")

db.commit()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	bot.clear_step_handler(message)
	msg = bot.send_message(message.chat.id, 'Введите имя: ')
	bot.register_next_step_handler(msg, start_answer_one)

def start_answer_one(message):
	global f_name
	f_name = message.text

	msg = bot.send_message(message.chat.id, 'Введите фамилию: ')
	bot.register_next_step_handler(msg, start_answer_two)

def start_answer_two(message):
	l_name = message.text

	sql.execute("SELECT * FROM users")
	sql.execute("INSERT INTO users VALUES (?, ?)", (f_name, l_name,))
	db.commit()

	markup = types.InlineKeyboardMarkup()
	resetDataKey = types.InlineKeyboardButton("Next", callback_data="next")
	markup.add(resetDataKey)

	bot.send_message(message.chat.id, "Жмите Next, чтобы добавить еще --->", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def inline_handler(call):
    if call.data == "next":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)


bot.infinity_polling()
