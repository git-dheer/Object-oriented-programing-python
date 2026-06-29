class Person :
    def __init__(self, name , age ):
        self.name = name
        self.age = age

    def greet (self):
        print (f"Hello my name is {self.name} and i am {self.age} years old.")
    
person1 = Person("Ram" ,"25")
person1.greet()