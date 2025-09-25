import sys 
sys.path.append('..')

import requests
import allure
import pytest
from data import TestData
from helpers import *
from urls import URLs

class TestCreateCourier:
    @allure.title('Тест создания курьера')
    def test_create_courier_true(self, courier_generate_and_delete):
        response = requests.post(URLs.URL_CREATE_COURIER, data = courier_generate_and_delete) # Создаем курьера
        assert (response.status_code == 201 and 
                response.json() == TestData.Message_Courier_Created_OK) # проверяем, что запрос возвращает правильный код ответа и текст сообщения
        
    @allure.title('Тест создания двух одинаковых курьеров')
    def test_create_duplicate_courier_false(self, courier_generate_and_delete):
        requests.post(URLs.URL_CREATE_COURIER, data = courier_generate_and_delete) # Создаем курьера1
        response_second = requests.post(URLs.URL_CREATE_COURIER, data = courier_generate_and_delete) # Создаем курьера2 и читаем ответ
        assert (response_second.status_code == 409 and 
                response_second.json() == TestData.Message_Courier_Conflict) # проверяем, что запрос возвращает правильный код ответа и текст сообщения

    @allure.title('Тест создания курьера, если одного из полей нет')
    @pytest.mark.parametrize('courier_payload', [ # логин и пароль являются обязательными, имя необязательное
                                       {'login': '', 'password': generate_password(), 'firstname': generate_first_name()},
                                       {'login': generate_login(), 'password': '', 'firstname': generate_first_name()},
                                       ])
    def test_create_courier_without_field_false(self, courier_payload):
        response = requests.post(URLs.URL_CREATE_COURIER, data = courier_payload) # Создаем курьера
        assert (response.status_code == 400 and 
                response.json() == TestData.Message_Courier_Bad_Request) # проверяем, что запрос возвращает правильный код ответа и текст сообщения
