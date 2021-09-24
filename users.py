class user():
    def __init__(self,firstname,lastname,age,phonenumber):
        self.name = firstname
        self.lastname = lastname
        self.age = age
        self.phonenumer = phonenumber
        self.login_attempts = 0

    def gretting(self):
        print("hello "+self.name+" "+self.lastname+ ". its very nice to see you")

    def describeuser(self):
        print("here are the basic information:-\n")
        print("first name: "+self.name)
        print("last name: "+self.lastname)
        print("age: "+str(self.age))
        print("phone number: "+str(self.phonenumer))

    def increment_login_attampts(self):
        self.login_attempts = self.login_attempts+1

    
    def reset_login_attampts(self):
        self.login_attempts = 0


















######################################################################################
##############################################################################
##################################################################
###########################################################



## creating an instance of class user

user1 = user("Amit","kumar",20,234332)


## calling the methods of the class user as USER1
user1.gretting()
user1.describeuser()





user1.increment_login_attampts()
user1.increment_login_attampts()
user1.increment_login_attampts()

print("\n")
print("this user has tried to log in "+str(user1.login_attempts)+ " times.")



user1.reset_login_attampts()

print("\n")
print("this user has tried to log in "+str(user1.login_attempts)+ " times.")



