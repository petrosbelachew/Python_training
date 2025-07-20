class MyClass:
    def __init__(self):
        print(f'{self} was  initialized')

    def a_method(self):
       print(f'called a_method on {self} ')
    def __str__(self):
        return 'Instance of MyClass'

class Horse:
   def trot(self):
       print('clop clop clop')

obj=MyClass()
horse1=Horse()
str1="Hello"

print(obj)
print(horse1)
print(str1)
print(type(horse1))
obj.a_method()
horse1.trot()

