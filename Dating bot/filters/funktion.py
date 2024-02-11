from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove


from keyboard.keyboards import ButtonText, get_on_start_kb
from keyboard.keyboards2 import ButtonMale, get_on_male



router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Доброго дня! Мене звати Jaster і я вам дпоможу знайти друзів або другу половинку.", reply_markup=get_on_start_kb())
    


@router.message(F.text == ButtonText.START)
async def meeting(message: Message):
    await message.answer(f"Для початку дізнаємось ваше ім'я", reply_markup=ReplyKeyboardRemove())



@router.message(F.text.regexp(r'^[a-zA-Zа-яА-Я\s]+$'))
async def handle_name(message: Message):
    await message.answer(f'Добре, тепер дізнаємось вашу стать.', reply_markup=get_on_male())



@router.message(F.text.in_([ButtonMale.WOMAN, ButtonMale.MAN]))
async def age(message: Message):
    await message.answer(text='Тепер, скільки вам років?', reply_markup=ReplyKeyboardRemove())



@router.message(F.text.regexp(r'\d+'))
async def handle_digits_message(message: Message):
    await message.answer("Добре, з якого ви міста, села?")
    
    

@router.message(F.text.regexp(r'^[a-zA-Zа-яА-Я\s]+$'))
async def city(message: Message):
    await message.answer('Тепер відправте свої фото або відео. Ви можете відправити до трьох фото або одне відео!')    
