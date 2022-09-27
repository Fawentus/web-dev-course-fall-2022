from fastapi import APIRouter
from app.data_base import DataBase
from app.user import User

auth_router = APIRouter(prefix="/auth")
data_base = DataBase()

@auth_router.post("/register")
def register(user: User):
    """
    Registration of a new user in the database
    """
    data_base.register(login=user.login, pswd=user.pswd, name=user.name)

@auth_router.post("/add_fan_fiction")
def add_fan_fiction(user: User, fan_fiction: str = ""):
    """
    Add new fan_fiction in the database
    """
    return data_base.add_fan_fiction(id=user.id, fan_fiction=fan_fiction)

@auth_router.get("/get_fan_fictions")
def get_fan_fictions():
    """
    Get all fan_fictions from the database
    """
    return data_base.fan_fictions

@auth_router.get("/get_users")
def get_users():
    """
    Get all users from the database
    """
    return data_base.users