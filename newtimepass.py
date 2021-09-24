class haha():

    def __init__(self,name):
        self.name = name
        self.number = 500

    def nameprint(self):
        print(self.name)
    
    def numberprint(self):
        print(self.number)

    def resetnumber(self):
        self.number = 0

user1 = haha("sandeep")


print(user1.number)

user1.resetnumber()

print(user1.number)