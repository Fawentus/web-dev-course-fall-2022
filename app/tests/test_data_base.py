import pytest
from app.data_base import DataBase
from app.user import User
from app.exceptions import AlreadyRegisteredError, UserNotFoundError

test_user = User(
    login="test",
    pswd="test",
    name="test"
)

right_user = User(
    id=0,
    login="test",
    pswd="test",
    name="test",
    fan_fictions_id=[],
)

right_user_whith_fan_fiction = User(
    id=0,
    login="test",
    pswd="test",
    name="test",
    fan_fictions_id=[0],
)

wrong_user = User(
    id=1,
    login="wrong",
    pswd="wrong",
    name="wrong",
    fan_fictions_id=[]
)

test_db = DataBase()

def test_register():
    test_db.register(login=test_user.login, pswd=test_user.pswd, name=test_user.name)
    assert test_db.users == {0: right_user}
    assert test_db.logins == {0: "test"}
    assert test_db.fan_fictions == {}

def test_add_fan_fiction():
    assert 0 == test_db.add_fan_fiction(id=right_user.id, fan_fiction="test")
    assert test_db.users == {0: right_user_whith_fan_fiction}
    assert test_db.fan_fictions == {0: "test"}

def test_register_err():
    with pytest.raises(AlreadyRegisteredError):
        test_db.register(login=test_user.login, pswd=test_user.pswd, name=test_user.name)
        assert test_db.users == {0: right_user}
        assert test_db.logins == {0: "test"}
        assert test_db.fan_fictions == {}

def test_add_fan_fiction_err():
    with pytest.raises(UserNotFoundError):
        test_db.add_fan_fiction(id=wrong_user.id, fan_fiction="wrong")
        assert test_db.users == {0: right_user_whith_fan_fiction}
        assert test_db.fan_fictions == {0: "test"}