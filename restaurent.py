


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


class IceCreamStand(restaurant):
    def __init__(self, restaurant_name, causine_type):
        super().__init__(restaurant_name, causine_type)
        self.flavors = ["vanilla","chocolate","dark choco","caramel"]


    def displayflavors(self):
        print("we are serving below flavors of icecream - ")
        for i in self.flavors:
            print(i)
        













######################################################################################
##############################################################################
##################################################################
###########################################################



mynewrestaurent = IceCreamStand("kulfiwala","ice creams")

mynewrestaurent.displayflavors()