# Why bad?
# Add more than 1 dog or cat?
# comments?
# variable names are trash
# updating anything is a pain (divergent changes)


class Bad:

    def __init__(self, name, dog, d_breed, d_age, cat, c_breed, c_age):
        # constructor
        self.n = name
        self.d = dog
        self.d_breed = d_breed
        self.d_age = d_age
        self.c = cat
        self.c_breed = c_breed
        self.c_age = c_age

    def update_dog(self, name, breed, age):
        self.d = name
        self.d_breed = breed
        self.d_age = age

    def update_cat(self, name, breed, age):
        self.c = name
        self.c_breed = breed
        self.c_age = age

    ### Display dog information
    def display_dog(self):
        print(f'{self.n} has 1 dog named {self.d} that is a {self.d_age} year old {self.d_breed}')

    ### Display cat information
    def display_cat(self):
        print(f'{self.n} has 1 cat named {self.c} that is a {self.c_age} year old {self.c_breed}')


if __name__ == "__main__":
    Bad('Alex', 'Bo', 'Foxhound', 3,  '', '', '').display_dog()
    Bad('David', '', '', '', 'Gray', 'gray cat', 1000).display_cat()
