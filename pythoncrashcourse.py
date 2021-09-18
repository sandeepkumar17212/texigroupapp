
## restaurant class excercise 9.1

class restaurant():
    def __init__(self,restaurant_name,causine_type):
        
            self.name = restaurant_name;
            self.causinetype = causine_type;
            self.number_served = 0;
        
    def describe_restaurant(self):
        print("Our restaurant "+ self.name + " is famous for "+self.causinetype)


    def open_restaurant(self):
        print("and "+self.name + " is open for the customers")



## 3 instances of restaurant excercise 9.2

grandhayat = restaurant("grand HAYAT", "Indian")
tajhotel = restaurant("Taj mumbai", "south indian food")
dabrihotel = restaurant("The Grand Dabri","Rajasthani Food")


grandhayat.describe_restaurant()
print("\n")
tajhotel.describe_restaurant()
print("\n")
dabrihotel.describe_restaurant()

## user class  excercise 9.3

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



user1 = user("sandeep","kumar",30,450343505)

user1.gretting()
user1.describeuser()

user2 = user("Amit","kumar",20,234332)

user2.gretting()
user2.describeuser()


