class user():
    def __init__(self,firstname,lastname,phonenumber):
        self.name = firstname
        self.lastname = lastname

        ## adding the age as a default value
        ## can be changed the value of age with the below method.
        self.age = 18
        self.phonenumer = phonenumber

    def printage(self):
        print("the age of "+self.name + " is "+ str(self.age))

    def updateage(self,age):
        if age<18:
            print("you need to be above 18 to perform this action")
        else:
            self.age = age

    def FirstAndLast(self,firstname,lastname):
        print(self.firstname+" "+self.lastname)



user1 = user("sandeep","kumar",450343505)

## changing the default value of the age attribute 
# (this is the first method to change the value of the age attribute).


##user1.age = 30

##user1.printage()

## second method of changing the value of age attribute by defining the mehtod 
# which can change the value of the attribute.

newage = input("add the new age you wish to change to - - ")
user1.updateage(int(newage))

user1.printage()



