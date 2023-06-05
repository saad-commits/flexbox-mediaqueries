# ek key ke corresponding value nikal sakte 
#pehle dict was unorderd , nnow after python 3.7 its ordered
dic={
    "saad":"daddy",
    "zaid":"son",
    344:"zaitoon"
    }
print(dic["saad"])
print(dic[344])  # gives proper eror
print(dic.get(3442)) # gives daddy saad value none if absent 
# output
#   daddy
#   saad


# abhi tak key ki values nikale 
# ab key ko kaise print karna hai

print(dic.items()) # print all pairs
print(dic.keys())  # print all keys
print(dic.values()) # print all values
# ya
for key in dic.keys():
    print( f"The key {key} corresponds to value {dic[key]}" )

# iterating pairs
for i in dic.items():
    print(f"One of item is {i}")

# iterating key and values seperately
for key,value in dic.items():
    print(f"The key {key} corresponds to value {value}")

