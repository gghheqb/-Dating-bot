from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ButtonDes:
    DESCRIPTION = 'Залишити пуcтим📃'

def get_on_description():
    button_description = KeyboardButton(text=ButtonDes.DESCRIPTION)
    buttons_row = [button_description]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return markup
