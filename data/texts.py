greeting_text = "\nРады приветствовать вас!\nВыберите, чем я могу вам помочь:"

choose_an_address_text = "Выберите адрес"

choose_date_text = "Веберите день когда хотите прийти"

choose_time_text = "Выберите время, когда Вы хотите приехать ?"

list_with_time = ["С 17:00", "С 18:00", "С 19:00", "С 20:00", "С 21:00",
                  "С 22:00", "С 23:00", "С 00:00", "С 01:00", "С 02:00", "С 03:00"]

we_are_closed = "К сожалению, на эту дату бронь оформить не получится"

rooms = \
    """
В это время свободны следующие
кабинки. Выберите, какая нравится
или измените время.
    """

get_name_text = \
    """
Осталось пару моментов и я
забронирую Вам кабинку.
Напишите, на чьё имя
забронировать?
    """

get_count_of_guests_text = "Какое количство человек будет?"

get_phone_number_text = \
    """
Напишите, пожалуйста, телефон,
чтобы администратор мог
связаться и подтвердить бронь
    """

final_book_text = \
    """
Благодарю! В ближайшее время
с Вами свяжется администратор
для подтверждения брони.
    """

filling_in_final_form = {
    "get_name": get_name_text,
    "count_of_guests": get_count_of_guests_text,
    "phone_number": get_phone_number_text,
    "final_text": final_book_text
}

texts = {
    "greetings": greeting_text,
    "addresses": choose_an_address_text,
    "date": choose_date_text,
    "time_select": choose_time_text,
    "times": list_with_time,
    "closed": we_are_closed,
    "rooms": rooms,
    "form_to_fill": filling_in_final_form
}
