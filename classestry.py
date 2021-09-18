class dog():
    def __init__(self,name,age,phone):
        self.name = name;
        self.age = age
        self.phone = phone

    def printname(self):
        print("my name is "+self.name)

    def phoneshow(self):
        print("my phone number is : "+self.phone)

student = dog("sandeep kumar")

student.printname()