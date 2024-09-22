from aiogram.fsm.state import State, StatesGroup

class Reg(StatesGroup):
    find_user = State()
    set_name = State()
    set_ras = State()

class Fight(StatesGroup):
    start = State()
    create_evil = State()
    choose = State()