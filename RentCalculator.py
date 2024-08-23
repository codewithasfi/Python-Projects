#Inputs from user
#Total rent
#total of food ordered for snacking
#Electricity units spent
#Charge per unit
#no. of ppl living in the flat

#Output
#total amount you have to pay

rent=int(input("Enter the rent of your hostel/flat:"))
food=int(input("Enter the amount of food ordered:"))
electricity_unit=int(input("Enter the amount electricity units spent:"))
charge_pu=int(input("Enter the amount of charge per unit of electricity:"))
person=int(input("Enter the number of flatmates:"))

total_electricity=electricity_unit*charge_pu

total_rent=(total_electricity+rent+food)//person

print("The amount of rent each person has to pay is",total_rent)
