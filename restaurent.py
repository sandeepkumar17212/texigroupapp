


class restaurant():
    def __init__(self,restaurant_name,causine_type):
        
            self.name = restaurant_name;
            self.causinetype = causine_type;
            self.number_served = 0;
        
    def describe_restaurant(self):
        print("Our restaurant "+ self.name + " is famous for "+self.causinetype)


    def open_restaurant(self):
        print("and "+self.name + " is open for the customers")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,numbers):
        self.number_served = self.number_served+numbers



grandhayat = restaurant("grand HAYAT", "Indian")
tajhotel = restaurant("Taj mumbai", "south indian food")
dabrihotel = restaurant("The Grand Dabri","Rajasthani Food")


grandhayat.describe_restaurant()
print("\n")
tajhotel.describe_restaurant()
print("\n")
dabrihotel.describe_restaurant()

print(grandhayat.number_served)



grandhayat.set_number_served(380)

print(grandhayat.number_served)

grandhayat.increment_number_served(5)

print(grandhayat.number_served)