import datetime

def express_delivery(num_items):
    if num_items <= 0:
        raise ValueError("Некорректное количество товаров")
    elif num_items == 1:
        return 10.95
    else:
        return 10.95 + 2.95 * (num_items - 1)

def delivery_decorator(func):
    def wrapper(num_items):
        start_time = datetime.datetime.now()
        result = func(num_items)
        end_time = datetime.datetime.now()
        print(f"Функция {func.__name__} вызвана в {start_time}")
        print(f"Количество товаров: {num_items}")
        print(f"Стоимость доставки: {result}")
        print(f"Время выполнения функции: {end_time - start_time}")
        return result
    return wrapper

express_delivery = delivery_decorator(express_delivery)

num_items = int(input("Введите количество товаров в заказе: "))
print(f"Общая стоимость доставки: {express_delivery(num_items)}")
