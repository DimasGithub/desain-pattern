class Product:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class ConcreteProduct1(Product):
    def __init__(self):
        super().__init__("ConcreteProduct1")


class ConcreteProduct2(Product):
    def __init__(self):
        super().__init__("ConcreteProduct2")


class Creator:
    def factory_method(self):
        raise NotImplementedError

    def some_operation(self):
        product = self.factory_method()
        result = "Creator: The same creator's code has just worked with "
        result += product.get_name()
        return result


class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2() 
