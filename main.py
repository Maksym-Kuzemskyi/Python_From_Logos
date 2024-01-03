import random


class Phone:
    __memory = 0
    __charger = False
    __usb_port = ''
    __diagonal = 0.0

    def __init__(self, memory: int, charger: bool, usb_port: str, diagonal: float):
        self.__memory = memory  # Приватна змінна пам'яті телефону в гігабайтах
        self.__charger = charger  # Приватний атрибут, чи має телефон зарядний пристрій
        self.__usb_port = usb_port  # Приватний атрибут, тип USB-порту
        self.__diagonal = diagonal  # Приватний атрибут, діагональ екрана у дюймах

    def generate_random_data(self):
        num_pairs = random.randint(1, 5)  # Випадкова кількість пар (від 1 до 5)
        key_value_pairs = {str(i): random.choice([1, 2.5, 'three']) for i in range(num_pairs)}
        keys = set(key_value_pairs.keys())
        values = set(str(value) for value in key_value_pairs.values())
        return keys, values

    # Методи для отримання значень приватних атрибутів
    def get_memory(self):
        return self.__memory

    def get_charger(self):
        return self.__charger

    def get_usb_port(self):
        return self.__usb_port

    def get_diagonal(self):
        return self.__diagonal

    # Методи-сетери для зміни значень приватних атрибутів
    def set_memory(self, new_memory):
        self.__memory = new_memory

    def set_charger(self, new_charger):
        self.__charger = new_charger

    def set_usb_port(self, new_usb_port):
        self.__usb_port = new_usb_port

    def set_diagonal(self, new_diagonal):
        self.__diagonal = new_diagonal


class Model(Phone):
    __model_name = ''
    __price = 0.0
    __core = ''

    def __init__(self, model_name: str, price: float, core: str,
                 memory: int, charger: bool, usb_port: str, diagonal: float):
        super().__init__(memory, charger, usb_port, diagonal)
        self.__model_name = model_name
        self.__price = price
        self.__core = core

    # Метод для зміни атрибутів об'єкту батьківського класу
    def change_phone_attributes(self, new_memory: int, new_charger: bool, new_usb_port: str, new_diagonal: float):
        self.set_memory(new_memory)  # Змінюємо пам'ять за допомогою сеттера
        self.set_charger(new_charger)  # Змінюємо зарядку за допомогою сеттера
        self.set_usb_port(new_usb_port)  # Змінюємо usb порт за допомогою сеттера
        self.set_diagonal(new_diagonal)  # Змінюємо діагональ за допомогою сеттера

    def generate_random_data(self):
        num_pairs = random.randint(1, 5)  # Випадкова кількість пар (від 1 до 5)
        key_value_pairs = {chr(65 + i): random.choice([True, False, 'some_value']) for i in range(num_pairs)}
        keys = set(key_value_pairs.keys())
        values = set(str(value) for value in key_value_pairs.values())
        return keys, values

    # Методи для отримання значень приватних атрибутів моделі
    def get_model_name(self):
        return self.__model_name

    def get_price(self):
        return self.__price

    def get_core(self):
        return self.__core

    # Методи-сеттери для зміни значень приватних атрибутів моделі
    def set_model_name(self, new_model_name):
        self.__model_name = new_model_name

    def set_price(self, new_price):
        self.__price = new_price

    def set_core(self, new_core):
        self.__core = new_core


# Створюємо об'єкти
my_phone = Phone(256, True, 'USB-C', 6.2)
my_model = Model('iPhone 13', 999.99, 'A14', 512, True, 'Lightning', 6.1)

# Викликаємо методи для генерації випадкових даних
phone_keys, phone_values = my_phone.generate_random_data()
model_keys, model_values = my_model.generate_random_data()

# Виведемо отримані дані для перевірки
print("Phone keys:", phone_keys)
print("Phone values:", phone_values)
print("Model keys:", model_keys)
print("Model values:", model_values)
