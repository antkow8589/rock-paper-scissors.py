"""
В данном модуле будут храниться две клавиатуры. Одна с кнопками "Давай!" и "Не хочу!",
 а вторая с игровыми кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜".
 Причем, для того, чтобы еще раз лучше понять разницу между созданием клавиатур
 с помощью билдера клавиатур и без него, реализуем оба варианта.
 Первая клавиатура будет с билдером, а вторая без.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicons.lexicon_ru import LEXICON_RU

#создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no = KeyboardButton(text=LEXICON_RU["no_button"])

#инициализируем билдер (устанавливаем билдер) для клавиатуры с кнопками "Давай" и "Не хочу"
yes_no_kb_builder = ReplyKeyboardBuilder()

#добавляем кнопки в билдер с аргументом width = 2
yes_no_kb_builder.row(button_yes,button_no, width=2)

#создаем клавиуатуру с кнопками "давай" и "не хочу"
"""
У клавиатуры yes_no_kb добавляем параметр one_time_keyboard=True, потому что эта клавиатура 
должна сворачиваться после нажатия пользователя на кнопку с текстом "Не хочу!". 
А если пользователь нажмет на кнопку "Давай!" - клавиатура yes_no_kb будет заменена на игровую клавиатуру. 
"""
yes_no_kb: ReplyKeyboardMarkup=yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------
# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)