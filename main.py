class ClassOne:
    def __init__(self, attr1):
        self.__attr1 = attr1

    def get_attr1(self):
        return self.__attr1

    def set_attr1(self, value):
        self.__attr1 = value


class ClassTwo:
    def __init__(self, attr1, attr2):
        self.__attr1 = attr1
        self.__attr2 = attr2

    def get_attr1(self):
        return self.__attr1

    def set_attr1(self, value):
        self.__attr1 = value

    def get_attr2(self):
        return self.__attr2

    def set_attr2(self, value):
        self.__attr2 = value


class ClassThree:
    def __init__(self, attr1, attr2, attr3):
        self.__attr1 = attr1
        self.__attr2 = attr2
        self.__attr3 = attr3

    def get_attr1(self):
        return self.__attr1

    def set_attr1(self, value):
        self.__attr1 = value

    def get_attr2(self):
        return self.__attr2

    def set_attr2(self, value):
        self.__attr2 = value

    def get_attr3(self):
        return self.__attr3

    def set_attr3(self, value):
        self.__attr3 = value


class ClassFour:
    def __init__(self, attr1, attr2, attr3, attr4):
        self.__attr1 = attr1
        self.__attr2 = attr2
        self.__attr3 = attr3
        self.__attr4 = attr4

    def get_attr1(self):
        return self.__attr1

    def set_attr1(self, value):
        self.__attr1 = value

    def get_attr2(self):
        return self.__attr2

    def set_attr2(self, value):
        self.__attr2 = value

    def get_attr3(self):
        return self.__attr3

    def set_attr3(self, value):
        self.__attr3 = value

    def get_attr4(self):
        return self.__attr4

    def set_attr4(self, value):
        self.__attr4 = value


def find_classes_with_methods(classes):
    method_dict = {}
    method_dict_2 = {}
    for class_ in classes:
        methods = [method for method in dir(class_) if callable(getattr(class_, method)) and method.startswith('get')]
        if len(methods) >= 1:
            if len(methods) == 1:
                method_dict[class_] = getattr(class_, methods[0])
            elif len(methods) == 2:
                method_dict[class_] = getattr(class_, methods[0])
                method_dict_2[class_] = getattr(class_, methods[1])
    return method_dict, method_dict_2


classes_list = [ClassOne, ClassTwo, ClassThree, ClassFour]

method_dict_1, method_dict_2 = find_classes_with_methods(classes_list)

print(method_dict_1)
print(method_dict_2)
