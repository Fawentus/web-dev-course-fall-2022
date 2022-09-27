from app.user import User
from app.exceptions import AlreadyRegisteredError, UserNotFoundError


class DataBase():
    def __init__(self) -> None:
        self.users = {}          # id -> user
        self.logins = {}         # id -> login
        self.fan_fictions = {}   # id_fan_fiction -> fan_fiction

    def register(self, login: str, pswd: str, name: str) -> User:
        """
        Regiseters user
        
        Params: login password and name of the new user
        Returns: registered user
        """
        if login in self.logins.values():
            raise AlreadyRegisteredError()
        
        id = len(self.logins)
        self.logins[id] = login
        user = User(
            id=id,
            login=login,
            pswd=pswd,
            name=name,
            fan_fictions_id=[],
        )
        self.users[id] = user
        return user

    def add_fan_fiction(self, id: int, fan_fiction: str) -> int:
        """
        Adding a fan_fiction by a user
        
        Params: id and new fan_fiction of user
        Returns: fan_fiction id
        """
        if id not in self.users:
            raise UserNotFoundError
        fan_fiction_id = len(self.fan_fictions)
        self.users[id].fan_fictions_id += [fan_fiction_id]
        self.fan_fictions[fan_fiction_id] = fan_fiction
        return fan_fiction_id