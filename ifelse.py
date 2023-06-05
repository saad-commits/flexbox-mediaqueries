# a=int(input("Enter your age"))
# print("Your age is" , a )

# if(a>=18):
#     print("you can drive")
# else:
#     print("You cant drive")

# # print(a>18)
# # print(a<18)
# # print(a==18)
# # print(a!=18)



# name=input("Enter tour name")

# if(name=="saad"):
#     print("you are valid user")
# else:
#     print("chala jaa bhos****")

# num= int(input("Enter a number to be tested "))

# if(num>0):
#     print("The number is positive")
# elif(num==0):
#     print("number is neutral")
# else:
#     print("the number is negative")

#  #elif hamesha upar se neeche jaata hai , jaisa condition satisfies it exit the whole cindition

num=int(input("enter a number"))
if(num<0):
    print("The number is -ve")
elif(num>0):
    if(num <=10):
        print("Num is in between 1-10")
    elif(num>10 and num <=20):
        print("num is between 10 and 20")
    else:
        print("Num is greater than 20")
else:
    print("The number is 0")
