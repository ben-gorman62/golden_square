from lib.todo_list import *
import pytest

def test_list_init():
    todo_list = TodoList()
    assert todo_list.list == []

def test_add_task():
    todo_list = TodoList()
    todo_list.add_task("Walk the dog")
    assert todo_list.list == ["Walk the dog"]

def test_add_three_tasks():
    todo_list = TodoList()
    todo_list.add_task("Walk the dog")
    todo_list.add_task("Walk the plank")
    todo_list.add_task("Walk the walk")
    assert todo_list.list == ["Walk the dog", "Walk the plank", "Walk the walk"]

def test_see_tasks():
    todo_list = TodoList()
    todo_list.add_task("Walk the dog")
    todo_list.add_task("Walk the plank")
    todo_list.add_task("Walk the walk")
    assert todo_list.see_tasks() == ["Walk the dog", "Walk the plank", "Walk the walk"]
    
def test_non_string_inputs():
    todo_list = TodoList()
    todo_list.add_task(None)
    todo_list.add_task(True)
    todo_list.add_task(983)
    assert todo_list.see_tasks() == ["None", "True", "983"]

def test_check_complete():
    todo_list = TodoList()
    todo_list.add_task("Walk the dog")
    todo_list.add_task("Walk the plank")
    todo_list.add_task("Walk the walk")
    assert todo_list.check_complete("Walk the plank") == "Task complete! Task removed from Todo List."
    assert todo_list.see_tasks() == ["Walk the dog", "Walk the walk"]

def test_task_not_in_list():
    todo_list = TodoList()
    with pytest.raises(ValueError) as err:
        todo_list.check_complete("Walk the plank")
    assert str(err.value)