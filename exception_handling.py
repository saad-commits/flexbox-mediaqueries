# erors comes for eg from server there is a problem and we dont want our 
# program to terminate 

# a=input("enter the number")
# print(f"Table of multipliction of {a} is")
# try:
#  for i in range(1,11): 
#        print(f"{a} X {i} = {int(a)*i}")
# except:
#       print("sorry invalid input")
# print("Some line of code")
# print("End of program")

#  # enter the number sa
#  # Table of multipliction of  sa is
#  # sorry
#  # End of program
#  # Some line of code


# try:
#  a=int(input("enter the number"))
#  print(f"Table of multipliction of {a} is")


#  for i in range(1,11):
#       print(f"{a} X {i} = {a*i}")
# except:
#       print("sorry invalid input")

# print("Some line of code")
# print("End of program") 

# # enter the number s
# # sorry 
# # Some line of code
# # End of program

#specific kind of eror
try:
    num=int(input("Enter an integer:"))
    a=[6,7]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index error")