# let's create some number fun inf the form of a ansible filter plugin

class FilterModule(object):

    def filters(self):
        return {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'modulo': self.modulo,
            'power': self.power,
        }

    def add(self, value, num):
        return value + num

    def subtract(self, value, num):
        return value - num

    def multiply(self, value, num):
        return value * num

    def divide(self, value, num):
        return value / num

    def modulo(self, value, num):
        return value % num

    def power(self, value, num):
        return value ** num

    def sum(self, value):
        return sum(value)