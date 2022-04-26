import datetime
import sqlalchemy
from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  #  Присваиваем каждому юзеру ешго id
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)   #  Есессна его имя
    town = sqlalchemy.Column(sqlalchemy.String, nullable=True)  #  Город юзера. По умолчанию - Москва
    register_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)  #  Дата регистрации, потом будем сообщать её юзеру
    chat_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)  #  Нужно для отправки юзеру сообщений
    requestsam = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)  #  Количество запросов погоды. Нужно, чтобы сообщать юзеру.

    def __repr__(self):
        return f'<User> {self.id} {self.name} {self.town} {self.register_date}'
