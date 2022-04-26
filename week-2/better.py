# Why better?
# extract class, updating a cat or dog doesn't impact the other objects

# Why bad?
# Add more than 1 dog or cat?
# comments?
# variable names are trash
# updating anything is a pain (divergent changes)


class Better:

    def __init__(self, name, dog, d_breed, d_age, cat, c_breed, c_age):
        self.name = name
        self.cat = Cat(cat, c_breed, c_age)
        self.dog = Dog(dog, d_breed, d_age)


class Cat:

    def __init__(self, cat, c_breed, c_age):
        self.cat = cat
        self.cat_breed = c_breed
        self.cat_age = c_age

    def update_cat(self, name, breed, age):
        self.cat = name
        self.cat_breed = breed
        self.cat_age = age

    def display(self, owner):
        print(f'{owner} has 1 cat named {self.cat} that is a {self.cat_age} year old {self.cat_breed}')


class Dog:

    def __init__(self, dog, d_breed, d_age):
        self.dog = dog
        self.dog_breed = d_breed
        self.dog_age = d_age

    def update_dog(self, name, breed, age):
        self.dog = name
        self.dog_breed = breed
        self.dog_age = age

    def display(self, owner):
        print(f'{owner} has 1 dog named {self.dog} that is a {self.dog_age} year old {self.dog_breed}')


if __name__ == "__main__":
    Better('Alex', 'Bo', 'Foxhound', 3,  '', '', '').dog.display('Alex')
    Better('David', '', '', '', 'Gray', 'gray cat', 1000).cat.display('David')
