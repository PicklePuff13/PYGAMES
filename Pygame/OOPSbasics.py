#creating a class

class person:
    name="Abi"
    age=16
    height=150

    def user(self):
        self.name=input("What's your name?")
        self.age=input("What's your height?")
        self.height=input("What's your height?")
    
    def out(self):
        print(self.name)
        print(self.age)
        print(self.height)
    
obj1=person()
print(obj1.name)
obj1.user()
obj1.out()