 # if you want to add remove item first convert tuple to list , then change 
#then list to upkle
countries=("India","china","saudi","russia","norway","turkey")
temp=list(countries)
temp.append("iran")  # add item
temp.pop(1) #remove item
print(temp)
countries=tuple(temp) 

# #concat direct two tuples 
# # tuple1= tuple2+tuple3
print(countries)
how=countries.count("china") # no of occurance 
print(how)
index=countries.index("India")
index1=countries.index("saudi",1,5) # find index of saudi bet 2-5
print(index1)
index2=countries.index("russia",0,3) 
print(index2)

      