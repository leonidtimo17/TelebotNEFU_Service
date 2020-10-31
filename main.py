import telebot

bot = telebot.TeleBot("1234330845:AAEBrmJw8hbAeqC10A2wPNDIHdJa3dev_BU")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard1.add('Регистрация', 'Востановления пароля', 'Тех.Поддержка')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '👋Здравстуйте выберите кнопку корторая расположена снизу ',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'регистрация':
        bot.send_message(message.chat.id, '✅Для регистрации указываете ФИО, дату рождения и паспортные данные ')
        bot.send_message(message.chat.id, '✅После этого нажимаете на "Проверить" ')
        bot.send_message(message.chat.id,
                         '✅На следующей странице выбираете нужный логин и указываете пароль (они будут использоваться для входа в личный кабинет) и указываете телефон и email (Email используется для активации аккаунта и восстановления пароля) ')
        bot.send_message(message.chat.id,
                         '✅Далее на указанный email придет ссылка для активации аккаунта и после этого можете зайти на свой личный кабинет. ')
        bot.send_message(message.chat.id,
                         'Или посмотрите видеоролик📺:                                                                https://www.youtube.com/watch?v=nhMT3TcCyGQ',
                         reply_markup=keyboard1)
    elif message.text.lower() == 'востановления пароля':
        bot.send_message(message.chat.id, '✅На сайте есть кнопка восстановления пароля')
        bot.send_message(message.chat.id, '✅Куда указываете свою личную эл.почту, которую указывали при регистрации. ')
        bot.send_message(message.chat.id,
                         '✅Далее на этот email придет ссылка для сброса пароля и после перехода к нему можете ввести новый пароль. ')
        bot.send_message(message.chat.id,
                         '✅Если вы не помните логин и email, который указывали при регистрации, то надо аналогично регистрации заполнить свои данные и нажать на "Проверить" после если вы уже зарегистрированы, то покажет, ваш логин и email.',
                         reply_markup=keyboard1)
    elif message.text.lower() == 'тех.поддержка':
        bot.send_message(message.chat.id, '✉️Пресс-служба press-service@s-vfu.ru                                     '
                                          '📞Телефон: +7 (4112) 49-65-40', reply_markup=keyboard1)
    elif message.text.lower() == 'спасибо':
        bot.send_message(message.chat.id, 'Мы рады что вам помогли', reply_markup=keyboard1)


bot.polling()
