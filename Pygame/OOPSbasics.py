#creating a class

class person:
    name="Abi"
    age=16
    height=150
    #constructor-to initialise the values
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def user(self):
        self.name=input("What's your name?")
        self.age=input("What's your age?")
        self.height=input("What's your height?")
    
    def out(self):
        print(self.name)
        print(self.age)
        print(self.height)
    
obj1=person("Daisy",13,122)
obj2=person("Stuti",34,100)
obj3=person("Belle",12,99)
obj1.out()
obj2.out()
obj3.out()
obj1.user()
obj1.out()

