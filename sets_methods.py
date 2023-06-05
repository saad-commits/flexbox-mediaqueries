s1={1,2,3,4,5,6}
s2={1,3,4,5,6,7,8}

print(s1.union(s2))
# iske baad s1 and s2 untouched the , but agar s1 and s2 update hojaye to
s1.update(s2) # matlab s2 ke values in s1 me le aao
print(s1,s2)

print(s1.intersection(s2))
print(s1,s2)
s1.intersection_update(s2)
print(s1,s2)

#symetric difference
# (a union b) - (a intersection b)

#differnce 
#a-b
print(s1.difference(s2))
print(s1.difference_update(s2))

#isdisjoint
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))

#remove # discard 
# dono same kaam karte 
s1.remove(1)
# agar set me 1 rahega to remove discard dono chalega
# agar 1 nahi rahega to remove eror dega aur discard nahi

sa =s1.pop()
# last value pop hogi par koi bhi ho sakti hai as 
# set are unordered

s3={1,2,3,4,5,7,5,2}
del s3# 
#s3 will be deleted 

s3.clear()

# if a value exits 
if 2 in s1:
    print("saad")
else:
    print("saad-smart")