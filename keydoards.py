from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клава "Старт"
kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ИНФОРМАЦИЯ'),
            KeyboardButton(text='РАСCЧИТАТЬ НОРМУ КАЛОРИЙ'),
            KeyboardButton(text='КУПИТЬ')
        ]
    ], resize_keyboard=True
)

# Inline-клава "Калории"
kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Расчет нормы', callback_data='calories'),
            InlineKeyboardButton(text='Формула расчета', callback_data='formulas')
        ]
    ], resize_keyboard=True
)

# Inline-клаву "Продукт"
"""
изменил нумерацию с учетом картинок(5-9)
"""
kb_product = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт5', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт6', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт7', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт8', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт9', callback_data='product_buying')
        ]
    ], resize_keyboard=True
)
