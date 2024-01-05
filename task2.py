class CustomObject:
    def __init__(self, key, value_str, value_num):
        self.key = key
        self.value_str = value_str
        self.value_num = value_num


def create_objects_from_dict(dictionary):
    objects_list = []
    for key, value in dictionary.items():
        if isinstance(key, str):
            obj = CustomObject(key, value[0], value[1])
            objects_list.append(obj)
    return objects_list


# Приклад словника
my_dict = {('a', 'b'): ['hello', 10], 'c': ['world', 20], 123: ['not included', 30]}

# Створення списку об'єктів на основі словника
objects = create_objects_from_dict(my_dict)

# Виведення атрибутів створених об'єктів
for obj in objects:
    print(f"Key: {obj.key}, Value (str): {obj.value_str}, Value (num): {obj.value_num}")
