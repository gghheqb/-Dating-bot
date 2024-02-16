from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove

from keyboard.keyboards import ButtonText, get_on_start_kb
from keyboard.keyboards2 import ButtonMale, get_on_male
from keyboard.description import ButtonDes, get_on_description
from keyboard.search import ButtonSearch, get_on_searche
from keyboard.save import ButtonSave, get_on_save

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Доброго дня! Мене звати Jaster і я вам дпоможу знайти друзів або другу половинку.", reply_markup=get_on_start_kb())
    
@router.message(F.text == ButtonText.START)
async def age(message: Message):
    await message.answer('Для початку дізнаємось ваш вік', reply_markup=ReplyKeyboardRemove())
    
@router.message(F.text.regexp(r'\d+'))
async def name(message: Message):
    await message.answer('Тепер дізнаємось вашу стать', reply_markup=get_on_male())
    
@router.message(F.text.in_([ButtonMale.WOMAN, ButtonMale.MAN]))
async def seaerch(message: Message):
    await message.answer('Тепер дізнаємось кого ти шукаєш', reply_markup=get_on_searche())
    
@router.message(F.text.in_([ButtonSearch.MALE, ButtonSearch.FEMALE]))
async def 