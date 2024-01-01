from datetime import datetime


class MyClass:
    def __init__(self, public_attr, protected_attr, private_attr):
        self.public_attr = public_attr  # Публічний атрибут
        self._protected_attr = protected_attr  # Захищений атрибут
        self.__private_attr = private_attr  # Приватний атрибут

    def get_private_attr(self):
        return self.__private_attr

    def set_public_attr(self, new_value):
        self.public_attr = new_value
        self._write_to_file("Edited public attribute")

    def set_protected_attr(self, new_value):
        self._protected_attr = new_value
        self._write_to_file("Edited protected attribute")

    def set_private_attr(self, new_value):
        self.__private_attr = new_value
        self._write_to_file("Edited private attribute")

    def _write_to_file(self, action):
        with open("log.txt", "a") as file:
            timestamp = datetime.now().replace(microsecond=0)
            file.write(f"{timestamp}: Object {self} - {action}\n")


obj = MyClass("Public", "Protected", "Private")

# Зміна публічного атрибуту та запис до файлу
obj.set_public_attr("New Public Value")

# Зміна захищеного атрибуту та запис до файлу
obj.set_protected_attr("New Protected Value")

# Зміна приватного атрибуту та запис до файлу
obj.set_private_attr("New Private Value")
