from boart import *
from dctatpin_of_bot import *
from states import *
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
import pickle
from rpg import *

router = Router()


@router.message(StateFilter(Reg.set_name))
async def per(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Выберите расу", reply_markup=kb_rows(Hero.ras))
    await state.set_state(Reg.set_ras)


@router.message(StateFilter(Reg.set_ras))
async def fight(message: Message, state: FSMContext):
    a = dict(await state.get_data())
    await state.set_state(Fight.start)
    if message.text in Hero.ras :
        hero = Hero.create_hero(a["name"], message.text)
    else:
        hero =  Hero.create_hero(a["name"], a["ras"])
    await state.update_data(ras=message.text, hero=pickle.dumps(hero))
    await message.answer(f"Твои статы:\n{hero}")
    await message.answer(f"Лети птенчик имя:{a['name']}"
                         f"", reply_markup=kb_rows(["ту би контию", "рестарт"]))