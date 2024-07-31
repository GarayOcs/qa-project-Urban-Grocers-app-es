import sender_stand_request
import data
import pytest

@pytest.fixture
def auth_token():
    new_user = sender_stand_request.create_count(data.user_body)
    response_data = new_user.json()
    if 'authToken' not in response_data:
        raise Exception(f"Error: 'authToken' no se encontró en la respuesta. Respuesta completa: {response_data}")
    return response_data['authToken']

def positive_assert(kit_body):
    new_user = sender_stand_request.create_count(data.user_body)
    token = new_user.json().get('authToken')
    new_kit = sender_stand_request.create_kit(kit_body, token)
    assert new_kit.status_code == 201

def negative_assert(kit_body):
    new_user = sender_stand_request.create_count(data.user_body)
    token = new_user.json().get('authToken')
    new_kit = sender_stand_request.create_kit(kit_body, token)
    assert new_kit.status_code == 400

def test_create_kit_name_length_1():
    kit_body = {"name": "a"}
    positive_assert(kit_body)

def test_create_kit_name_length_511():
    kit_body = {"name": "Abcd" * 127 + "a"}
    positive_assert(kit_body)

def test_create_kit_name_length_0():
    kit_body = {"name": ""}
    negative_assert(kit_body)

def test_create_kit_name_length_512():
    kit_body = {"name": "Abcd" * 128}
    negative_assert(kit_body)

def test_create_kit_name_special_chars():
    kit_body = {"name": "!@#$%^&*()"}
    positive_assert(kit_body)

def test_create_kit_name_with_spaces():
    kit_body = {"name": " A Aaa "}
    positive_assert(kit_body)

def test_create_kit_name_with_numbers():
    kit_body = {"name": "123"}
    positive_assert(kit_body)

def test_create_kit_no_name():
    kit_body = {}
    negative_assert(kit_body)

def test_create_kit_name_as_number():
    kit_body = {"name": 123}
    negative_assert(kit_body)
