# lists bahot imp hota hai 
#    List is used to collect items that usually consist 
#    of elements of multiple data types. An array is also a vital
#    component that collects several items of the same data type.

# list - ek naam ke andar multiple cheez rakhna hai 
l1 =[1,2,3,4,5,6,"saad"]
# print(l1)
# print(type(l1))
# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3])
# print(l1[-4])

# lists me multiple data type aa sakte hai 

# *********************list are mutable ************************
# *********************tupple are immutable********************


# for list use
# if 7 in l1:
#     print("yes")
# else:
#     print("no")

# if "saad" in l1:
#     print("yes")

#for string use
# if "saa" in "saad":
#     print("yes")
# else:
#     print("no")

# #how to print all elements in list yaad kar yaad kar
# print(l1[:])
# print(l1)

# print(l1[1:-1])
# print(l1[1:7:2])  # jump index

# what is list comprehension , matlab on the flow list generte karre

list=[i*i for i in range(10)]
print(list)
list=[i for i in range(10) if i%2==0]
print(list)