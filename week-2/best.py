# Why best?
# Extract Class
# Extract SubClass
# Extract Method



class Best:

    def __init__(self, name):
        self.name = name
        self.cats = []
        self.dogs = []

    def add_pet(self, type, name, breed, age):
        if type == 'cat':
            self.cats.append(Cat(name, breed, age))
        elif type == 'dog':
            self.dogs.append(Dog(name, breed, age))

    def display_pets(self):
        for p in self.cats + self.dogs:
            p.display(self.name)


class Animal:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.type = self.__class__.__name__

    def display(self, owner):
        print(f'{owner} has a {self.type} named {self.name} that is a {self.age} year old {self.breed}')


class Cat(Animal):

    def __init__(self, cat, breed, age):
        super().__init__(cat, breed, age)

    def purr(self):
        print('Meow')


class Dog(Animal):

    def __init__(self, dog, breed, age):
        super().__init__(dog, breed, age)

    def woof(self):
        print('BARK BARK BARK')


if __name__ == "__main__":
    alex = Best('Alex')
    alex.add_pet('dog', 'Bo', 'Foxhound', 3)
    alex.add_pet('dog', 'Marni', 'Golden Doodle', 1)
    alex.dogs[1].woof()
    alex.display_pets()
    david = Best('David')
    david.add_pet('cat', 'Gray', 'gray cat', 1000)
    david.cats[0].purr()
    david.display_pets()