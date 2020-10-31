import telebot
bot = telebot.TeleBot("1234330845:AAEBrmJw8hbAeqC10A2wPNDIHdJa3dev_BU")
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Регистрация', 'Условие_2')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == 'регистрация':
        bot.send_message(message.chat.id,'Перейдите по ссылке чтобы понять как пройти регистрацию')

    elif message.text.lower() == 'условие_2':
        bot.send_message(message.chat.id, 'Выбрано_условие_2')
        keyboard2.row('Условие_5', 'Условие_6')

bot.polling()