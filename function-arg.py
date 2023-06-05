# def average(a,b):
#     print("the average is ",(a+b)/2)

# average(10,20)


#default arguemenmts 
# def average(a=1,b=2):
#     print("the average is ",(a+b)/2)
    # average(5) agar sirf a dena hai to 
    # average(b=9)    agar sirf b dena hai to 



# def name(fname, mname="Jhom", lname="whatson"):
#     print("hello", fname,mname,lname)

# name("saad")



 #variable length arguements 
def average(*numbers):    # 3 this takes number as tuple
     sum=0              
     for i in numbers:
         sum = sum + i
     #print("the average is " , sum /(len(numbers)) )
     return sum /(len(numbers))
    # agar do returen statement lagege to pehla return statement execute hoga

c= average(5,5,4,6,6,6,6,6,5,54,34,33,2) 
print(c)







