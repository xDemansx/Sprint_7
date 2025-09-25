import sys 
sys.path.append('..')

# Ссылки для тестирования сайта
class URLs:

    URL_SAMOKAT = 'https://qa-scooter.praktikum-services.ru' # Главная страница сайта "Яндекс Самокат"
    URL_CREATE_COURIER = f'{URL_SAMOKAT}/api/v1/courier' # Courier - Создание курьера
    URL_LOGIN_COURIER = f'{URL_SAMOKAT}/api/v1/courier/login' # Courier - Логин курьера в системе
    URL_DELETE_COURIER = f'{URL_SAMOKAT}//api/v1/courier' # Courier - Удаление курьера
    URL_CREATE_ORDER = f'{URL_SAMOKAT}/api/v1/orders' # Orders - Создание заказа
    URL_GET_ORDERS_LIST = f'{URL_SAMOKAT}/api/v1/orders' # Orders - Получение списка заказов
    URL_CANCEL_ORDER = f'{URL_SAMOKAT}/api/v1/orders/cancel' # Orders - Отменить заказ
    URL_END_OF_ORDER = f'{URL_SAMOKAT}/api/v1/orders/finish/' # Orders - Завершить заказ
