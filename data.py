import sys 
sys.path.append('..')

class TestData:
    
    Order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }

    Message_Courier_Created_OK = {'ok': True}
    Message_Courier_Conflict = {"message": "Этот логин уже используется"}
    Message_Courier_Bad_Request = {"message": "Недостаточно данных для создания учетной записи"}
    Message_Courier_Not_Found = {"message": "Учетная запись не найдена"}
