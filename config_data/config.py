'''
Файл с конфигурационными данными для бота, базы данных
'''
from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token:str  #токен для доступа к телеграмм боту
@dataclass
class Config:
    tg_bot:TgBot

def load_config(path:str | None=None)->Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))

