class Car():
    ##A simple attempt to represent a car.
    def __init__(self, make, model, year):
    ##Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
    ##Return a neatly formatted descriptive name.
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        ##print the statement to show the odometer reading.
        return("this car has "+str(self.odometer_reading)+" miles on it")
    
    ## updating odometer using a method
    def update_odometer(self,milage):
        if milage>=self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("Sorry, you cannt rollback the meter reading")

    def increment_odometer(self, miles):
    ##Add the given amount to the odometer reading.
        self.odometer_reading += miles



class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battry_size = 70
    


    def describe_battery(self):
        print("this car has a "+str(self.battry_size)+" kWh battery.")









######################################################################################
##############################################################################
##################################################################
###########################################################



## creating an instance of class "Car"
my_new_car = Car('audi', 'a4', 2016)


## calling methods of class "Car"


##get full name
print(my_new_car.get_descriptive_name())

##updating odometer 
my_new_car.update_odometer(400)
print(my_new_car.read_odometer())

##trying to rollback the meter. haha (i know this will give me an error message.)
my_new_car.increment_odometer(300)
print(my_new_car.read_odometer())


print("-------------------------------------------------------------")

mycar = ElectricCar("tesla","m3",2025)
print(mycar.get_descriptive_name())
mycar.describe_battery()