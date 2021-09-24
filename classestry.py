class dog():
    def __init__(self,name,age,phone):
        self.name = name;
        self.age = age
        self.phone = phone
        self.balance = 50000

    def printname(self):
        print("my name is "+self.name)

    def phoneshow(self):
        print("my phone number is : "+self.phone)

    def update_balance(self,kitnaadd):
        self.balance = kitnaadd

student = dog("sandeep kumar",24,5534422)

student.printname()
student.balance = 200000000
print(student.balance)

student.update_balance(2344293)

print(student.balance)