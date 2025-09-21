import sys 
sys.path.append('..')

import requests
import json
import allure
import pytest
from urls import URLs
from data import TestData


class TestCreateOrder:
    @allure.title("Тест создания заказа")
    @allure.description("Проверь, что, когда создаёшь заказ: можно указать один из цветов — BLACK или GREY; " \
    "можно указать оба цвета; можно совсем не указывать цвет; тело ответа содержит track.")
    @pytest.mark.parametrize('colour', ['BLACK', 'GREY', ['BLACK', 'GREY'], '']) # Используем параметризацию 
    def test_create_order_with_different_colour_true(self, colour):
        TestData.Order_data['color'] = [colour] # Передаем цвет
        order_data_json = json.dumps(TestData.Order_data)
        response = requests.post(URLs.URL_CREATE_ORDER, data=order_data_json)
        assert (response.status_code == 201 and 'track' in response.text) # Сверяем код ответа и тело ответа

        track = response.json()['track'] # Получаем номера заказа
        requests.post(f'{URLs.URL_END_OF_ORDER}/{track}') # Orders - Завершить заказ
