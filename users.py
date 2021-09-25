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


