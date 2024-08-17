#!/usr/bin/env python
'''
This program will help you a great deal 
learning about classes and objects
'''

import sys

class Animal:
    '''
    Base Class Definition of type Animal
    '''

    #Class object variables - variables that every instance of this class will have
    sheltered = True
    leftpawed=False

    def __init__(self, name, breed, color, nickname='doggo', vaccinated=True, trained=False):
        #Name mangling
        self.__nickname = nickname

        #private attributes
        self._vaccinated=vaccinated
        self._trained=trained
        self._color=color
        
        #standard attributes
        self.name=name
        self.breed=breed

    @staticmethod #using the staticmethod decorator
    def bark():
        #Generic implementation of bark method that should be implemented  
        #in child classes by override
        print('Bark Bark')


class Dog(Animal):
    '''
    Child class definition of Dog with reference to parent Class Animal
    '''
    
    def __str__(self): #dunder methods
        return f'This is an dog object with name as {self.name}'

    @staticmethod
    def __del__(): #Dunder methods defined in the class using staticmethod decorator
        print(f'Dog object has been deleted')

    def who_am_i(self): #standard method
       print(f'I am a fun loving dog of breed {self.breed}. I am {self._color} in color and  my name is {self.name}')

    @staticmethod
    def bark(): #standard method defined in the class using staticmethod decorator
       '''Dog will bark'''
       #Dog will bark
       print(f'I love to WOOF!')

    @property
    def color(self):
        print(f'Printing current color value for {self.name}')
        return self._color

    @color.setter
    def color(self, color_value):
        if self._color != color_value:
            self._color = color_value
            print(f'{self.name} color was changed to {self._color}')
        else:
            print(f'{self.name} color was not changed')

    #@color.deleter
    #def color(self):
    #    del self._color
    #    print(f'{self.name}\'s color was deleted')


def main():
    '''
    This is the main function. This function will be called when this program runs as script
    '''

    dogname = input("Pl enter the Dog's name: ")
    breedname = input('Pl enter the breed\'s name: ')
    colorname = input('What color is your dog: ')

    #instantiate an object           
    my_dog1 = Dog(dogname, breedname, colorname)
    my_dog1.who_am_i()
    my_dog1.bark()

if __name__ == '__main__':
    print(f'The program was run as a script with name as {__name__}')
    sys.exit(main())

print(f'The program was imported as a module with module name as {__name__}')

##
##End of program


