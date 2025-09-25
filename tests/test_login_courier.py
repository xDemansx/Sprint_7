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
    def test_courier_login_full_data_true(self, courier_create_and_delete): 
        response = requests.post(URLs.URL_LOGIN_COURIER, data = courier_create_and_delete[0]) # Логиним курьера
        assert (response.status_code == 200 and 'id' in response.text)

    @allure.title('Тест логина курьера, при неверном логине')
    def test_courier_login_wrong_false(self, courier_create_and_delete):
        response = requests.post(URLs.URL_LOGIN_COURIER, data = courier_create_and_delete[1]) # Логиним курьера
        assert (response.status_code == 404 and response.json() == TestData.Message_Courier_Not_Found)

    @allure.title('Тест логина курьера, при неверном пароле')
    def test_courier_password_wrong_false(self, courier_create_and_delete):
        response = requests.post(URLs.URL_LOGIN_COURIER, data = courier_create_and_delete[2]) # Логиним курьера
        assert (response.status_code == 404 and response.json() == TestData.Message_Courier_Not_Found)

    @allure.title('Тест логина курьера, при незаполненном поле логин)')
    def test_courier_login_empty_false(self, courier_create_and_delete):
        response = requests.post(URLs.URL_LOGIN_COURIER, data = courier_create_and_delete[3]) # Логиним курьера
        assert (response.status_code == 400 and response.json() == TestData.Message_Courier_Bad_Request)

    @allure.title('Тест логина курьера, при незаполненном поле пароль)')
    def test_courier_password_empty_false(self, courier_create_and_delete):
        response = requests.post(URLs.URL_LOGIN_COURIER, data = courier_create_and_delete[4]) # Логиним курьера
        assert (response.status_code == 400 and response.json() == TestData.Message_Courier_Bad_Request)
