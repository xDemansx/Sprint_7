import sys 
sys.path.append('..')

import requests
import json
import allure
import pytest
from urls import URLs
from data import TestData


class TestGetListOrder:

    @allure.title('Тест получения списка заказов')
    def test_get_list_orders_trrue(self):
        list_orders = requests.get(URLs.URL_GET_ORDERS_LIST)
        assert (list_orders.status_code == 200 and 
                "orders" in list_orders.json())
        