# # factorial(7) =7*6*4*3*2*1

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return(n*factorial(n-1))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# fibonacci series f0=0 f1=1
# f0=0
# f1=1
# f2=f1+f0
# fn=f(n-1) + f(n-2)

# n=4
# def fibonacci(n):
#     if (n==0):
#          return 0
#     elif (n==1):
#         return 1
#     else :
#         c=fibonacci(n-1) + fibonacci(n-2)
#         return c

# for i in range(0,n):
#      print(fibonacci(i))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return(n*factorial(n-1))
# factorial_number=int(input("enter the number to get factorial of"))
# print(factorial(factorial_number))



fibo_len=int(input("Enter how mnay numbers fibonaccui series ypu want biatch"))

def fibonacci(fibo_len):
    if fibo_len==0:
        return 0
    elif fibo_len==1:
        return 1
    else:
        c= fibonacci(fibo_len-1) + fibonacci(fibo_len-2)
        return c
    


for i in range(0,fibo_len):
    print(fibonacci(i))
































