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

# Переменная для отслеживания состояния обработки имени
is_name_handled = False

# Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Доброго дня! Мене звати Jaster і я вам дпоможу знайти друзів або другу половинку.", reply_markup=get_on_start_kb())

# Обработчик кнопки "Почати"
@router.message(F.text == ButtonText.START)
async def meeting(message: Message):
    # Проверяем, было ли уже обработано имя
    global is_name_handled
    if not is_name_handled:
        # Если имя еще не было обработано, запрашиваем имя
        await message.answer(f"Для початку дізнаємось ваше ім'я", reply_markup=ReplyKeyboardRemove())
    else:
        # Если имя уже было обработано, запрашиваем город
        await message.answer('Тепер відправте свої фото або відео. Ви можете відправити до трьох фото або одне відео!')

# Обработчик для имени и города
@router.message(F.text.regexp(r'^[a-zA-Zа-яА-Я\s]+$') & ~F.text.in_([ButtonText.START, ButtonMale.WOMAN, ButtonMale.MAN, ButtonSave.SAVE]))
async def handle_name_or_city(message: Message):
    global is_name_handled
    if not is_name_handled:
        is_name_handled = True
        await message.answer(f'Добре, тепер дізнаємось вашу стать.', reply_markup=get_on_male())
    elif message.text == ButtonSave.SAVE:  # Check if the message text is equal to ButtonSave.SAVE
        await message.answer('Ок, тепер по бажанню можете написати опис до свого профілю. Розкажіть трохи про себе та кого тут шукаєте!', reply_markup=get_on_description())
    else:
        await message.answer('Тепер відправте свої фото або відео. Ви можете відправити до трьох фото або одне відео!')

# Обработчик для пола
@router.message(F.text.in_([ButtonMale.WOMAN, ButtonMale.MAN]))
async def age(message: Message):
    await message.answer(text='Тепер, скільки вам років?', reply_markup=ReplyKeyboardRemove())

# Обработчик для возраста
@router.message(F.text.regexp(r'\d+'))
async def handle_digits_message(message: Message):
    await message.answer("Добре, з якого ви міста, села?")

# Обработчик для города

 
    
any_media_filter = F.photo | F.video

# Змінна, що зберігає кількість фотографій, яка надійшла
photo_count = 0

@router.message(any_media_filter)
async def media(message: Message):
    global photo_count  # Оголошуємо глобальну змінну, щоб мати доступ до неї всередині функції
    if message.photo:
        photo_count += 1  # Якщо надійшла фотографія, збільшуємо лічильник на 1
        if photo_count <= 3:  # Перевіряємо, чи не перевищено ліміт в 3 фотографії
            await handle_photo(message, photo_count)  # Передаємо лічильник як номер фотографії
        else:
            await message.answer("Максимальна кількість фотографій досягнута.")
    elif message.video:
        await handle_video(message)
    else:    
        await message.answer("Забороняється відправляти фото інтимного характеру!")
        
async def handle_photo(message: Message, photo_number: int):
    if photo_number < 3:
        await message.answer(f'{photo_number}/3 Ви можете відправити ще одне фото, якщо хочете.', reply_markup=get_on_save())
    else:
        await message.answer(f'Це ваше останнє фото. Будь ласка, по бажанню додайте опис до вашого профілю або натисніть кнопку нижче', reply_markup=get_on_description())
        # Тут можна викликати іншу функцію або взяти іншу дію в залежності від вашого варіанту.
        
@router.message(F.text == ButtonSave.SAVE)
async def handle_video(message: Message):
    await message.answer('Ок, тепер по бажанню можете написати опис до свого профілю. Розкажіть трохи про себе та кого тут шукаєте!', reply_markup=get_on_description())


   
   
    
@router.message(F.text == ButtonDes.DESCRIPTION)
async def description(message: Message):
    await message.answer('Добре, ми майже закінчили. Тепер дізнаємось кого ви шукаєте', reply_markup=get_on_searche())
    
@router.message(F.text.in_([ButtonSearch.MALE, ButtonSearch.FEMALE]))
async def search(message: Message):
    await message.answer(f'Все готово. Тепер перевірте свою анкету і якщо все добре починаємо вам пошук)', reply_markup=ReplyKeyboardRemove())