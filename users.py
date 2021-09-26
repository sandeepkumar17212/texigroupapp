
## "user" class is defining the user and can be called by
## providing firstname,lastname,age,phonenumber.

class user():
    def __init__(self,firstname,lastname,age,phonenumber):
        self.name = firstname
        self.lastname = lastname
        self.age = age
        self.phonenumer = phonenumber
        self.login_attempts = 0
    

    
    ## gretting method to greet the user.
    def gretting(self):
        print("hello "+self.name+" "+self.lastname+ ". its very nice to see you")
    
    ## describe method to discribe the user.
    def describeuser(self):
        print("here are the basic information:-\n")
        print("first name: "+self.name)
        print("last name: "+self.lastname)
        print("age: "+str(self.age))
        print("phone number: "+str(self.phonenumer))
    ## method which can be used to increase the login attemp. 
    def increment_login_attampts(self):
        self.login_attempts = self.login_attempts+1

    ## method to reset the login attempts.
    def reset_login_attampts(self):
        self.login_attempts = 0



## "Admin" is a child class of the class "user"
class Admin(user):
    
    ## here defining the attribute we need to pass to call admin class (this
    ## should be same attribute as in "user" class.)
    def __init__(self, firstname, lastname, age, phonenumber):
        super().__init__(firstname, lastname, age, phonenumber)
        self.privileges = Privileges().privileges

    def showprivileges(self):
        Privileges().showprivileges()

    


class Privileges():
    def __init__(self):
        
        self.privileges = ["can add post","can delete post","can edit post","can ban user"]


    def showprivileges(self):
        print("below are the actions you can perform-")
        for i in self.privileges:
            print(i)




newdriver = Admin("sandeep","kumar",34,4838347)

newdriver.describeuser()

################################################################

#newpre = Privileges(newdriver.privileges)
print("--------------------------ffff-------------------")
newdriver.showprivileges()
##########################################



