import requests


URL = "https://df-react-todo-client-class.herokuapp.com"


def test_get_todos():
    response = requests.get(URL + "/todos")
    assert response.ok


def test_add_todo():
    pass


def test_delete_todo():
    pass


def test_complete_todo():
    pass
