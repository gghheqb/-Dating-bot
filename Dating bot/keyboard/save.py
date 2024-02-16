from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ButtonSave:
    SAVE = 'Зберегти'

def get_on_save():
    button_description = KeyboardButton(text=ButtonSave.SAVE)
    buttons_row = [button_description]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return markup
