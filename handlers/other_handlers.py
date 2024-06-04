from aiogram import Router
from aiogram.types import Message
from lexicons.lexicon_ru import LEXICON_RU

router = Router()

#хендлер для сообщений которые не попали в другие хендлеры
#При декорировании хэндлера, мы не устанавливаем никакие фильтры,
# то есть этот хэндлер будет срабатывать на любые сообщения от пользователя.
@router.message()
async def send_answer(message:Message):
    await message.answer(text=LEXICON_RU["other_answer"])
