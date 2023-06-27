import telebot

bot = telebot.TeleBot("5669397682:AAE_U46PXxsk4bXXHKKRH62FbJFfbHmaz5c")

guilanfood_button = telebot.types.InlineKeyboardButton('Guilan Food', url= 'http://food.guilan.ac.ir')
guilanecent_button = telebot.types.InlineKeyboardButton("Guilan Ecent", url= 'http://ecent2.guilan.ac.ir')
guilansada_button = telebot.types.InlineKeyboardButton("nguilansada",url= 'https://sada.guilan.ac.ir/Hermes')

guilanfood_markup = telebot.types.InlineKeyboardMarkup()
guilanfood_markup.add(guilanfood_button)

guilanecent_markup = telebot.types.InlineKeyboardMarkup()
guilanecent_markup.add(guilanecent_button)

guilansada_markup = telebot.types.InlineKeyboardMarkup()
guilanecent_markup.add(guilansada_button)

guilanall_markup = telebot.types.InlineKeyboardMarkup(row_width= 1)
guilanall_markup.add(guilanfood_button,guilanecent_button,guilansada_button)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id,"hi Java k/j/oooon , welcome to this fucking stupid bot\nI'm glad i can speak with you and i wish i work properly :)")

@bot.message_handler(comands=['help'])
def helpme(message):
    bot.send_message(message.chat.id, ' available commands are:\nhelp\nstart\nguila\
                     nfood\nguilanecent\nguilansada\nallGuilan')

@bot.message_handler(commands=['guilanfood'])
def guilanfood(message):
    bot.send_message(message.chat.id,"here is the link and the direct button below\nhttp://food.guilan.ac.ir",reply_markup=guilanfood_markup)

@bot.message_handler(commands=['guilanecent'])
def guilanfood(message):
    bot.send_message(message.chat.id,"here is the link and the direct button below\nhttp://ecent2.guilan.ac.ir",reply_markup=guilanecent_markup)

@bot.message_handler(commands=['guilansada'])
def guilanfood(message):
    bot.send_message(message.chat.id,"here is the link and the direct button below\nhttps://sada.guilan.ac.ir/Hermes",reply_markup=guilansada_markup)

@bot.message_handler(commands=['guilanall'])
def guilanall(message):
    bot.send_message(message.chat.id,"here are all guilan websites direct link",reply_markup=guilanall_markup)


bot.infinity_polling()