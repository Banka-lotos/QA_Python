
class Animal:
    def __init__(self,name):
        self.name = name


    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f'{self.name} say ГАВ ГАВ ГАВ'
   
class Cat(Animal):
    def speak(self):
        return f"{self.name} say МЯУ ГДЕ ЕДА "
   
dog = Dog('Гром')
cat = Cat('Йота')




print(dog.speak())
print(cat.speak())
