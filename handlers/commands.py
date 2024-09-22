from boart import *
from dctatpin_of_bot import *
from states import *
from utils import *
from states import *
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.fsm.state import default_state


router = Router()


@router.message(Command("start"), StateFilter(default_state))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer("вы можете начать игру введите команду /reg"
                         )

'''@router.message(Command('start'), ~StateFilter(default_state))
async def start_ng(message: Message, state: FSMContext) -> None:
    await message.answer("Закончить игру?", reply_markup=kb_rows(["Завершить", "Продолжить игру"]))

@router.message(F.text.in_(("Завершить", "Продолжить игру")), ~StateFilter(default_state))
async def chos_ac(message: Message, state: FSMContext):
    fi = message.text
    if fi == "Завершить":
        await state.set_state()
    else:
        pass'''


@router.message(Command("reg"))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.set_name)
    await message.answer("ведите имя")

