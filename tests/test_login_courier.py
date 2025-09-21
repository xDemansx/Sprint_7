import sys 
sys.path.append('..')

import requests
import allure
import pytest
from data import TestData
from helpers import *
from urls import URLs

class TestLoginCourier():
    @allure.title('Тест логина курьера со всеми обязательными полями')
    def test_courier_login_full_data_true(self):
        courier_payload = register_new_courier_and_return_login_password() # Данные для курьера
        requests.post(URLs.URL_CREATE_COURIER, data = courier_payload) # Создаем курьера
        response = requests.post(URLs.URL_LOGIN_COURIER, data = courier_payload) # Логиним курьера
        assert (response.status_code == 200 and 'id' in response.text)

    @allure.title('Тест логина курьера, при неверных логин/пароль')
    def test_courier_login_invalid_data_false(self):
        courier_payload = {'login': generate_login(), 'password': generate_password()} # Данные для курьера
        response = requests.post(URLs.URL_LOGIN_COURIER, data=courier_payload) # Логиним курьера
        assert (response.status_code == 404 and response.json() == TestData.Message_Courier_Not_Found)

    @allure.title('Тест логина курьера, при незаполненном поле логин)')
    def test_courier_login_empty_field_false(self):
        courier_payload = register_new_courier_and_return_login_password() # Данные для курьера
        requests.post(URLs.URL_CREATE_COURIER, data = courier_payload) # Создаем курьера
        payload_1 = {
        "login": '',
        "password": courier_payload['password']
        }
        response = requests.post(URLs.URL_LOGIN_COURIER, data=payload_1) # Логиним курьера
        assert (response.status_code == 400 and response.json() == TestData.Message_Courier_Bad_Request)

    @allure.title('Тест логина курьера, при незаполненном поле пароль)')
    def test_courier_login_empty_field_false(self):
        courier_payload = register_new_courier_and_return_login_password() # Данные для курьера
        requests.post(URLs.URL_CREATE_COURIER, data = courier_payload) # Создаем курьера
        payload_1 = {
        "login": courier_payload['login'],
        "password": ''
        }
        response = requests.post(URLs.URL_LOGIN_COURIER, data=payload_1) # Логиним курьера
        assert (response.status_code == 400 and response.json() == TestData.Message_Courier_Bad_Request)
