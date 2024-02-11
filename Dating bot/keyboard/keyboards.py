from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ButtonText:
    START = 'Почнемо знайомства👌'

def get_on_start_kb():
    button_start = KeyboardButton(text=ButtonText.START)
    buttons_row = [button_start]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return markup


    
