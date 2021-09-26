class dog():
    def __init__(self,name,age):
        self.name = name;
        self.age = age
        self.phone = "0450343505"
        self.balance = 50000

    def printname(self):
        print("my name is "+self.name)

    def phoneshow(self):
        print("my phone number is : "+self.phone)

    def update_balance(self,kitnaadd):
        self.balance = kitnaadd


class guardDog(dog):
    def __init__(self, name, age,protection):
        super().__init__(name, age)
        self.protection = protection


    def protuctedtime(self):
        print("he has protected us "+str(self.protection)+" times.")













student = dog("sandeep kumar",24)

student.printname()
student.balance = 200000000
print(student.balance)

student.update_balance(2344293)

print(student.balance)

print("_________________________________________________________________________________")

ratu = guardDog("Ratu",6,10)
print(ratu.name)
ratu.printname()
ratu.protuctedtime()