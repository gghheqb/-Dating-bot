from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class ButtonMale:
    MAN = 'Чоловік'
    WOMAN = 'Дічина'


def get_on_male():
    button_man = KeyboardButton(text=ButtonMale.MAN)
    button_woman = KeyboardButton(text=ButtonMale.WOMAN)
    buttons_row = [button_man, button_woman]
    markup = ReplyKeyboardMarkup(keyboard = [buttons_row], resize_keyboard=True)
    return markup