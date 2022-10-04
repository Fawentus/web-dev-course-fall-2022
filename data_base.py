import user_pb2
import user_pb2_grpc
import exceptions


class DataBase():
    def __init__(self) -> None:
        self.users = {} # id -> user
        self.names = {} # id -> name

    def register(self, name: str) -> int:
        """
        Regiseters user
        
        Params: name of the new user
        Returns: id registered user
        """
        if name in self.names.values():
            raise exceptions.NameAlreadyRegisteredError()
        
        id = len(self.names)
        self.names[id] = name
        user = user_pb2.UserData()
        user.id = id
        user.name = name
        user.count_trees = 0
        self.users[id] = user
        return id

    def plant(self, id: int) -> str:
        """
        Increases count of trees
        
        Params: id user
        Returns: message
        """
        if id not in self.users:
            raise exceptions.UserNotRegisteredError()
        self.users[id].count_trees += 1
        return "You planted a tree!"

    def cutDown(self, id: int) -> str:
        """
        Decreases count of trees
        
        Params: id user
        Returns: message
        """
        if id not in self.users:
            raise exceptions.UserNotRegisteredError()
        if self.users[id].count_trees > 0:
            self.users[id].count_trees -= 1
            return "You cut down a tree!"
        return "You have not a tree :("