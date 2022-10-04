import pytest
from data_base import DataBase
from user_pb2 import UserData
import exceptions

test_db = DataBase()

@pytest.mark.parametrize("test_input,expected", [
    (UserData(
        name="test1",
        id=-1,
        count_trees=0),
    UserData(
       name="test1",
        id=0,
        count_trees=0)),
    (UserData(
        name="test2",
        id=-1,
        count_trees=0),
    UserData(
       name="test2",
        id=1,
        count_trees=0))])
def test_register(test_input, expected):
    test_input.id = test_db.register(name=test_input.name)
    assert test_db.users[expected.id] == expected
    assert test_db.names[expected.id] == expected.name

@pytest.mark.parametrize("test_input,expected", [
    (UserData(
       name="test1",
        id=0,
        count_trees=0),
    UserData(
       name="test1",
        id=0,
        count_trees=0)),
    (UserData(
       name="test2",
        id=1,
        count_trees=0),
    UserData(
       name="test2",
        id=1,
        count_trees=0))])
def test_plant(test_input, expected):
    assert test_db.users[test_input.id].count_trees == expected.count_trees
    test_db.plant(test_input.id)
    expected.count_trees += 1
    assert test_db.users[test_input.id].count_trees == expected.count_trees
    
    test_db.plant(test_input.id)
    expected.count_trees += 1
    test_db.plant(test_input.id)
    expected.count_trees += 1
    test_db.plant(test_input.id)
    expected.count_trees += 1
    assert test_db.users[test_input.id].count_trees == expected.count_trees
    
@pytest.mark.parametrize("test_input,expected", [
    (UserData(
       name="test1",
        id=0,
        count_trees=4),
    UserData(
       name="test1",
        id=0,
        count_trees=4)),
    (UserData(
       name="test2",
        id=1,
        count_trees=4),
    UserData(
       name="test2",
        id=1,
        count_trees=4))])
def test_cutDown(test_input, expected):
    assert test_db.users[test_input.id].count_trees == expected.count_trees
    test_db.cutDown(test_input.id)
    expected.count_trees -= 1
    assert test_db.users[test_input.id].count_trees == expected.count_trees
    
    test_db.cutDown(test_input.id)
    expected.count_trees -= 1
    test_db.cutDown(test_input.id)
    expected.count_trees -= 1
    test_db.cutDown(test_input.id)
    expected.count_trees -= 1
    assert test_db.users[test_input.id].count_trees == expected.count_trees

    test_db.cutDown(test_input.id)
    assert test_db.users[test_input.id].count_trees == expected.count_trees


@pytest.mark.parametrize("test_input,expected", [
    (UserData(
       name="test1",
        id=-1,
        count_trees=0),
    UserData(
       name="test1",
        id=0,
        count_trees=0)),
    (UserData(
       name="test2",
        id=-1,
        count_trees=0),
    UserData(
       name="test2",
        id=1,
        count_trees=0))])
def test_register_err(test_input, expected):
    with pytest.raises(exceptions.NameAlreadyRegisteredError):
        test_register(test_input, expected)

@pytest.mark.parametrize("err_id", [-1, 2, 3])
def test_plant_err(err_id):
    with pytest.raises(exceptions.UserNotRegisteredError):
        test_db.plant(id=err_id)

@pytest.mark.parametrize("err_id", [-1, 2, 3])
def test_cutDown_err(err_id):
    with pytest.raises(exceptions.UserNotRegisteredError):
        test_db.cutDown(id=err_id)