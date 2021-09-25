
import caller

import users

import restaurent





######################################################################################
##############################################################################
##################################################################
###########################################################




caller.printname("sandeep kumar")






## creating an instance of class user


user1 = users.user("Amit","kumar",20,234332)


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





######################################################################################
##############################################################################
##################################################################
###########################################################
#####  after this restaurent class methods are written.






## created the instances of the class restaurant 

grandhayat = restaurent.restaurant("grand HAYAT", "Indian")
tajhotel = restaurent.restaurant("Taj mumbai", "south indian food")
dabrihotel = restaurent.restaurant("The Grand Dabri","Rajasthani Food")

## calling the methods of class RESTAURANT
grandhayat.describe_restaurant()
print("\n")
tajhotel.describe_restaurant()
print("\n")
dabrihotel.describe_restaurant()

## printing the default atttibute of the class
print(grandhayat.number_served)


## calling a method to set the value of number served and printing its value
grandhayat.set_number_served(380)

print(grandhayat.number_served)


## calling a method to increment the number served and then printing it. 
grandhayat.increment_number_served(5)

print("At Grand Hayat, we have served "+ str(grandhayat.number_served) + "customers TODAY")

