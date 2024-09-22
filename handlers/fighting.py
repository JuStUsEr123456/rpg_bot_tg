from boart import *
from states import *
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
import random as r
import pickle
from handlers.reg import fight


router = Router()

@router.message(Fight.start, F.text == "ту би контию")
async def pre_fighting(message: Message, state: FSMContext):
    await state.set_state(Fight.create_evil)
    await figh_evil(message=message, state=state)


@router.message(Fight.start, F.text == "рестарт")
async def fighting(message: Message, state: FSMContext):
    await message.answer("Введите имя")
    await state.set_state(Reg.set_name)


@router.message(Fight.create_evil)
async def figh_evil(message: Message, state: FSMContext):
    evil = BAD_BOY.create_enemy()
    await state.update_data(bad=pickle.dumps(evil))
    await state.set_state(Fight.choose)
    await message.answer(f"вы встретили злодея {evil}")
    await message.answer("готов с ним сразиться?", reply_markup=kb_rows(["бей", "беги"]))

async def op_faht(message: Message, state: FSMContext,bad_data, hero_data):
    results_enemy = bad_data.ataka(hero_data)
    if results_enemy:
        await state.update_data(hero=pickle.dumps(hero_data), bad=pickle.dumps(bad_data))
        await message.answer("Тебя побили не будь тряпкой ударь в отовет твои зровя ровна")
        await message.answer(f"Чуть чуть осталось давай я веру в тебя")
        await message.answer(f"Готов ли ты срозиться c {bad_data} ", reply_markup=kb_rows(["бей", "беги"]))
    else:
        await state.update_data(hero=None, bad=None)
        await message.answer("ты проиграл")
        await message.answer("Неудачник(проигравший) расу менять будешь?!!!!!!!!!")
        await fight(message, state)


@router.message(Fight.choose, F.text == "бей")
async def yes_fight(message: Message, state: FSMContext):
    ddb = await state.get_data()
    hero_data = pickle.loads(ddb["hero"])
    bad_data = pickle.loads(ddb["bad"])
    hero_data.ataka(bad_data)
    results = hero_data.ataka(bad_data)
    if not results:
        await message.answer(f"легенда пала")
        await state.update_data(bad=None, hero=pickle.dumps(hero_data))
        await state.set_state(Fight.create_evil)
    else:
        await op_faht(message, state, bad_data, hero_data)


@router.message(Fight.choose, F.text == "беги")
async def running(message: Message, state: FSMContext):
    p = r.randint(0, 1)
    ddb = await state.get_data()
    hero_data = pickle.loads(ddb["hero"])
    bad_data = pickle.loads(ddb["bad"])
    if p == 0:
        await state.set_state(Fight.create_evil)
        await message.answer("тебе повезло тебя не побили")
        await figh_evil(message, state)
    else:
        await op_faht(message, state, bad_data, hero_data)


@router.message()
async def ad(message: Message):
    await message.answer("Такая опция не доступна, пожалуста воспользуйтесь клавиатурой")