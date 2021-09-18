


class restaurant():
    def __init__(self,restaurant_name,causine_type):
        
            self.name = restaurant_name;
            self.causinetype = causine_type;
        
    def describe_restaurant(self):
        print("Our restaurant "+ self.name + " is famous for "+self.causinetype)


    def open_restaurant(self):
        print("and "+self.name + " is open for the customers")



grandhayat = restaurant("grand HAYAT", "Indian")
tajhotel = restaurant("Taj mumbai", "south indian food")
dabrihotel = restaurant("The Grand Dabri","Rajasthani Food")


grandhayat.describe_restaurant()
print("\n")
tajhotel.describe_restaurant()
print("\n")
dabrihotel.describe_restaurant()



