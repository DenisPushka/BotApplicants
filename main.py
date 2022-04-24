import telebot
from telebot import types
from utility import SMILE

bot = telebot.TeleBot('5377363272:AAGsDsaudhSMiCL6S8pV5025xJ6Rgi1tU5A')

array = [types.KeyboardButton(SMILE[1] + "Финансовые вопросы"),
         types.KeyboardButton("Военная кафедра СамГТУ"),
         types.KeyboardButton("Местонахождение общежитий СамГТУ"),
         types.KeyboardButton("Баллы для поступления в Самарский Политех"),
         types.KeyboardButton("Даты при поступлении"),
         types.KeyboardButton("Договор на целевое обучение"),
         types.KeyboardButton("Для иностранных граждан"),
         types.KeyboardButton("Для лиц с ограниченными возможностями здоровья"),
         types.KeyboardButton("С какого числа начинается прием документов?")
         ]


@bot.message_handler(commands=['start'])
def start(message):
    markupButton = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for val in array:
        markupButton.add(val)
    bot.send_message(message.chat.id, "Информация для аббитуриентов: ", reply_markup=markupButton)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == SMILE[1] + "Финансовые вопросы"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Кредит на свое обучение",
                                              url="https://priem.samgtu.ru/pages/education-credit"))
        markup.add(types.InlineKeyboardButton("Заключение договора об оказании платных образовательных услуг",
                                              url="https://samgtu.ru/bachelors/bachelors-contract"))
        markup.add(types.InlineKeyboardButton("Скидки на обучение",
                                              url="https://priem.samgtu.ru/pages/targeted-training"))
        bot.send_message(message.chat.id, text="Выбери вопрос: ", reply_markup=markup)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for val in array:
            markup.add(val)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "С какого числа начинается прием документов?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for val in array:
            markup.add(val)
        bot.send_message(message.chat.id, text='С 20 июня', reply_markup=markup)
    elif (message.text == "Местонахождение общежитий СамГТУ"):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("Ссылка", url="https://priem.samgtu.ru/hostels"))
        bot.send_message(message.chat.id, "Местонахождение общежитий СамГТУ", reply_markup=markup)
    elif (message.text == "Военная кафедра СамГТУ"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка", url="http://military.samgtu.ru/"))
        bot.send_message(message.chat.id, "Военная кафедра СамГТУ", reply_markup=markup)
    elif (message.text == "Заключение договора на целевое обучение"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://priem.samgtu.ru/pages/targeted-training"))
        bot.send_message(message.chat.id, "Заключение договора на целевое обучение", reply_markup=markup)
    elif (message.text == "Для иностранных граждан"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://priem.samgtu.ru/pages/targeted-training"))
        bot.send_message(message.chat.id, "Информация для иностранных граждан", reply_markup=markup)
    elif (message.text == "Количество бюджетных мест на факультете"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://samgtu.ru/uploads/admission/2022/kcp_2022.pdf"))
        bot.send_message(message.chat.id, "Количество бюджетных мест на факультете", reply_markup=markup)
    elif (message.text == "Прием на обучение лиц с ограниченными возможностями здоровья"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://samgtu.ru/bachelors/bachelors-priem-na-obuchenie-liz-s-ogranichennymi-vozmozhnostyami-zdorovya"))
        bot.send_message(message.chat.id, "Прием на обучение лиц с ограниченными возможностями здоровья",
                         reply_markup=markup)
    elif (message.text == "Экзамены, которые нужно сдавать после окончания колледжа, для поступления"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://samgtu.ru/bachelors/bachelors-entrance-tests"))
        bot.send_message(message.chat.id, "Экзамены, которые нужно сдавать после окончания колледжа, для поступления",
                         reply_markup=markup)
    elif (message.text == "Прием на обучение лиц с ограниченными возможностями здоровья"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://samgtu.ru/bachelors/bachelors-priem-na-obuchenie-liz-s-ogranichennymi-vozmozhnostyami-zdorovya"))
        bot.send_message(message.chat.id, "Прием на обучение лиц с ограниченными возможностями здоровья",
                         reply_markup=markup)
    elif (message.text == "Даты при поступлении"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Даты при поступлении на бакалавриат",
                                              url="https://samgtu.ru/uploads/admission/2022/kalendar_bac.pdf"))
        markup.add(types.InlineKeyboardButton("Даты при поступлении в магистратуру",
                                              url="https://samgtu.ru/uploads/admission/2022/kalendar_mag.pdf"))
        markup.add(types.InlineKeyboardButton("Даты при поступлении на заочное отделение",
                                              url="https://samgtu.ru/uploads/admission/2022/kalendar_zo.pdf"))
        markup.add(types.InlineKeyboardButton("Основные даты для абитуриентов 2022",
                                              url="https://samgtu.ru/bachelors/bachelors-dates"))
        bot.send_message(message.chat.id, "Даты при поступлении", reply_markup=markup)
    elif (message.text == "Баллы для поступления в Самарский Политех"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Баллы для поступления",
                                              url="https://samgtu.ru/bachelors/bachelors-minimum-points"))
        markup.add(types.InlineKeyboardButton("Доп. баллы по индивидуальным достижениям",
                                              url="https://priem.samgtu.ru/pages/additional-ratings"))
        bot.send_message(message.chat.id, "Баллы для поступления в Самарский Политех", reply_markup=markup)
    elif (message.text == "Даты при поступлении"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Даты при поступлении на бакалавриат",
                                              rl="https://samgtu.ru/uploads/admission/2022/kalendar_bac.pdf"))
        markup.add(types.InlineKeyboardButton("Даты при поступлении в магистратуру",
                                              url="https://samgtu.ru/uploads/admission/2022/kalendar_mag.pdf"))
        markup.add(types.InlineKeyboardButton("Даты при поступлении на заочное отделение",
                                              url="https://samgtu.ru/uploads/admission/2022/kalendar_zo.pdf"))
        markup.add(types.InlineKeyboardButton("Основные даты для абитуриентов 2022",
                                              url="https://samgtu.ru/bachelors/bachelors-dates"))
        bot.send_message(message.chat.id, "Даты при поступлении", reply_markup=markup)
    elif (message.text == "Договор на целевое обучение"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://priem.samgtu.ru/pages/targeted-training"))
        bot.send_message(message.chat.id, "Договор на целевое обучение", reply_markup=markup)
    elif (message.text == "Для лиц с ограниченными возможностями здоровья"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка",
                                              url="https://samgtu.ru/bachelors/bachelors-priem-na-obuchenie-liz-s-ogranichennymi-vozmozhnostyami-zdorovya"))
        bot.send_message(message.chat.id, "Прием на обучение лиц с ограниченными возможностями здоровья",
                         reply_markup=markup)


bot.polling(none_stop=True)
