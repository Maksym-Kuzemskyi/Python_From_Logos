class MyClass:
    def __init__(self, attribute):
        self.check_attribute(attribute)

    @staticmethod
    def check_attribute(attribute):
        if not isinstance(attribute, str):
            raise TypeError("Атрибут повинен бути стрічкою")
        else:
            print("Атрибут відповідає вимогам")


# Приклад використання класу
try:
    obj = MyClass("перша стрічка")
except TypeError as e:
    print(e)

try:
    obj = MyClass(123)
except TypeError as e:
    print(e)

try:
    obj = MyClass(["список"])
except TypeError as e:
    print(e)
