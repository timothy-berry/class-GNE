#!/usr/bin/env python
'''
This program will help you a great deal 
learning about classes and objects
'''

import sys

class Animal():
    '''
    Base Class Definition of type Animal
    '''

    def __init__(self,name,breed,color):
        self.name=name
        self.breed=breed
        self.color=color

    def bark(self):
        #Generic implementation of bark method that should be implemented  
        #in child classes by override
        print('Bark Bark')


class Dog(Animal):
    '''
    Child class definition of Dog with reference to parent Class Animal
    '''

    def bark(self):
       '''Dog will bark'''
       #Dog will bark
       print(f'I love to WOOF!')

    def who_am_i(self):
       print(f'I am a fun loving dog of breed {self.breed}. I am {self.color} in color and  my name is {self.name}')


def main():
    '''
    This is the main function. This function will be called when this program runs as script
    '''

    dogname = input("Pl enter the Dog's name: ")
    breedname = input('Pl enter the breed\'s name: ')
    colorname = input('What color is your dog: ')

    #instantiate an object           
    my_dog1 = Dog(dogname, breedname, colorname)
    my_dog1.bark()
    my_dog1.who_am_i()

if __name__ == '__main__':
    sys.exit(main())

print(f'The program was run as a script with name as {__name__}')

##
##End of program


