class user():
    def __init__(self,firstname,lastname,age,phonenumber):
        self.name = firstname
        self.lastname = lastname
        self.age = age
        self.phonenumer = phonenumber

    def gretting(self):
        print("hello "+self.name+" "+self.lastname+ ". its very nice to see you")

    def describeuser(self):
        print("here are the basic information:-\n")
        print("first name: "+self.name)
        print("last name: "+self.lastname)
        print("age: "+str(self.age))
        print("phone number: "+str(self.phonenumer))



sandeep = user("sandeep","kumar",30,450343505)

sandeep.gretting()
sandeep.describeuser()

user2 = user("Amit","kumar",20,234332)

user2.gretting()
user2.describeuser()