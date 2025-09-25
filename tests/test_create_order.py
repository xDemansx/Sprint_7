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
    def test_create_order_with_different_colour_true(self, colour, cancel_order):
        order_data = TestData.Order_data
        order_data['color'] = [colour]
        order_data_json = json.dumps(order_data)
        response = requests.post(URLs.URL_CREATE_ORDER, data=order_data_json)
        track = response.json()['track'] # Получаем номера заказа
        cancel_order(track) # Вызываем фикстуру отмены заказа послек выполнения теста
        assert (response.status_code == 201 and 'track' in response.text) # Сверяем код ответа и тело ответа
