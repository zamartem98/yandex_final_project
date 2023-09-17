## Импорт данных и функции проверки
import sender_stand_request

##Функция позитивной проверки статуса кода
def positive_assert(track_order):
    order_response = sender_stand_request.get_order_track(track_order)
    assert order_response.status_code == 200

##Тест
def test_get_order_track_success_response():
    positive_assert(sender_stand_request.track_order)