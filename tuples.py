# tuple ko change nai kar skat , jaisa lists me append hota hai waise isme nai hota 
# list ----> [isme hota hai ]
# tuppe--->(isme hota hai )
t1=(1,2,3,4,5,6,7,8,9,10)
print(type(t1) , t1)

# one element which is meant to be tuple should be written as this always
t2=(1,)

saad=("s","d","f",1,2)
print(saad)
print(type(saad))

#for eg list
list=[1,2,3,4,5]
list[1]=100
print(list)

print(t1[-1])
print(t1[3])

if 3 in t1:
    print("yes it is biatch")

# slicing 
tup2=t1[1:4]
print(tup2)

# s1=[1]
# print(type(s1))
# d1=(1,)
# print(type(d1))
# h1="1"
# print(type(h1))