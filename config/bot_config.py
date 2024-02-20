from environs import Env
from dataclasses import dataclass

env = Env()
env.read_env()
ADMINS = [111113554, 565444321]


@dataclass()
class bot_config:
    token: str
    admins: list[int]


@dataclass()
class bot:
    config: bot_config


def set_bot_config() -> bot:
    return bot(bot_config(token=env('my_token1'), admins=ADMINS))
