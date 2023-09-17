## Импорт данных и библиотеки "requests" с функциями
##Замошников Артём 1 когорта - Дипломная работа. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=data.headers)
response = post_new_order(data.order_body)


track_order = response.json()["track"]

def get_order_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params={"t": track_order})