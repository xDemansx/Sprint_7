import sys 
sys.path.append('..')

import requests
import random
import string 
from urls import URLs
from faker import Faker

fake = Faker()

def generate_login(): # Генерируем login
    login = fake.text(8)[:-1] # Генерируем текст и удаляем точку
    return login

def generate_password(): # Генерируем password
    return fake.password()

def generate_first_name(): # Генерируем firstName
    return fake.first_name()


# метод возвращает список из логина, пароля и имени
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
    