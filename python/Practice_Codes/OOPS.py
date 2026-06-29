from random import randint
class Employee:
    language = "Python" #this is a class attribute
    salary = "120000"
    
    def GetInfo(self): #a function always requires self to work without error
        print(f"The salary is: {self.salary},\nThe language is: {self.language}")
    
    @staticmethod
    def greet():
        print("?good Morning!")
    
    def __init__(self): #this is called a Dunder method, any method starting with __ is dunder method
        print("this method automatically runs when a new opject is called")
harry = Employee()
harry.language = "Java_Script" #this is an instance attribute, it gets priority over class attribute
harry.GetInfo() #system reads this as Employee.GetInfo(harry)

class train:
    def __init__(self, trainno):
        self.trainno = trainno

    def bookings(self, fro, to):
        print(f"Your ticket for {self.trainno} from {fro} to {to} is booked")

    def GetStatus(self):
        print(f"The train {self.trainno} is running on time")

    def fare(self, fro, to):
        print(f"The fare for {self.trainno} from {fro} to {to} is {randint(222, 5555)}")

a = train(2599)
a.bookings("rampur", "khampur")
a.GetStatus()
a.fare("rampur", "khampur")