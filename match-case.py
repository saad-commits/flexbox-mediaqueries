x=int(input("enter the value of x "))
#x is a variable to match 
match x:
    case 0 :
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3 :
        print("x is 3")
    # case _:
    #     print("x is neither 0,1,2,3")
    case _ if x!=80:
        print(x, " is not equal to 80")
    case _ if x!= 90:
        print(x, " is not equal to 80")
    case _:
        print(x)

# x=int(input("enter a number"))
# match x:
#     case 1:
#         print("saad")
#     case 2:
#         print("maaz")
#     case _:
#         print("saadss")
#     case _ if x==90:
#         print("abra ca dabra ")