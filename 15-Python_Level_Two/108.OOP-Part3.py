# Interitance
class Animal():
    def __init__(self, isMammal):
        print('Animal is created!')
        self.isMammal = isMammal
    def eat(self):
        print('Animal is eating.')
    def loyal(self):
        print('Animal is loyal.')
    def Mammal(self):
        print('Animal is {}'.format(self.isMammal))
    def notMammal(self, isMammal):
        print('Animal is {}'.format(isMammal))

class Dog(Animal):
    def __init__(self):
    #def __init__(self, isMammal):
        #Animal.__init__(self, isMammal)
        print('Dog is created!')
    def bark(self):
        print('Dog is barking.')
    def loyal(self):
        print('Dog is too loyal.')

#dog = Dog(isMammal = True)
dog = Dog()
dog.eat()
dog.bark()
dog.loyal()
#dog.Mammal()
dog.notMammal(isMammal=True)

# Special Method
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return self.title
    def __len__(self):
        return self.pages
    def __del__(self):
        print('Book is destroyed!')

book = Book('Ts', 'rajoriyas', 200)
print(book)
print(len(book))
#del book
