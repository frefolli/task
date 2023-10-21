import os
import datetime

def get_current_user() -> str:
    return os.getlogin()

def get_home_path() -> str:
    return os.getenv("HOME")

def get_current_datetime() -> datetime.datetime:
    return datetime.datetime.now()

def get_current_date() -> datetime.datetime:
    return get_current_datetime().date()

def get_current_time() -> datetime.datetime:
    return get_current_datetime().time()

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.mkdir(path)

def read_datetime(rep: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(rep)

def read_date(rep: str) -> datetime.date:
    return datetime.date.fromisoformat(rep)

def read_time(rep: str) -> datetime.time:
    return datetime.time.fromisoformat(rep)
