import datetime

from peewee import *

from utils_env import get_file_path

db = SqliteDatabase(get_file_path("rss.db"))


class BaseModel(Model):
    class Meta:
        database = db


class Rss(BaseModel):
    feed = CharField(unique=True)
    title = CharField(max_length=20)
    url = CharField(max_length=255)


class History(BaseModel):
    url = CharField(max_length=255)
    publish_at = DateField(default=datetime.datetime.now)


def create_tables():
    with db:
        db.create_tables([Rss, History])
