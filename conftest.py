import allure
import pytest
import requests
from data import *
from helpers import *

@pytest.fixture(scope='function')
def courier_generate_and_delete(): # Генерация данных курьера и удаление курьера
    courier = NewCourierLoginPassword.payload # Данные для курьера
    yield courier
    login_result = requests.post(f'{URLs.URL_LOGIN_COURIER}', data = NewCourierLoginPassword.data_courier[0]) # Логиним курьера
    r = login_result.json()
    requests.delete(f'{URLs.URL_DELETE_COURIER}/{r["id"]}', data = login_result) # Удаляем курьера по 'id'

@pytest.fixture(scope='function')
def courier_create_and_delete(): # Генерация данных, создание курьера и удаление курьера
    courier = NewCourierLoginPassword.payload # Данные для курьера
    requests.post(URLs.URL_CREATE_COURIER, data = courier) # Создаем курьера с полными данными
    courier_data = NewCourierLoginPassword.data_courier
    yield courier_data
    login_result = requests.post(f'{URLs.URL_LOGIN_COURIER}', data = NewCourierLoginPassword.data_courier[0]) # Логиним курьера с верными login и password
    r = login_result.json()
    requests.delete(f'{URLs.URL_DELETE_COURIER}/{r["id"]}', data = login_result) # Удаляем курьера по 'id'

@pytest.fixture
def cancel_order(): # Отмена созданного заказа
    track_ids = []
    # Возвращаем функцию для регистрации track
    def register_track_id(track):
        track_ids.append(track)
    yield register_track_id  # Передаем функцию в тест
    
    # После завершения теста удаляем все зарегистрированные заказы
    for track in track_ids:
        with allure.step('Отменяем заказ'):
            requests.put(URLs.URL_CANCEL_ORDER, params={"track": track}) # Отменить заказ
