from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class ButtonSearch:
    MALE = 'Чоловіка'
    FEMALE = 'Дічину'


def get_on_searche():
    button_male = KeyboardButton(text=ButtonSearch.MALE)
    button_female = KeyboardButton(text=ButtonSearch.FEMALE)
    buttons_row = [button_male, button_female]
    markup = ReplyKeyboardMarkup(keyboard = [buttons_row], resize_keyboard=True)
    return markup