# docstrings and pep-8
def square(n):
    '''takes in a number n , returns the square of n'''  # ye comment nai hai special string hai , function ki body ke upar likha jaata hai
    #A Python docstring is a string used to document a Python module, class, 
    # function or method, so programmers can understand what it does
    #  without having to read the details of the implementation. 
    # Also, it is a common practice 
    # to generate online (html) documentation automatically from docstrings
    print(n**2)
square(5)
print(square.__doc__)

# doc string hamesha hamesh right below funcion name ya right above function name
 # pep-8 python enhancement proposal 