# try except ke saath finally use karte hai clean up ke liye 
# finally ka code hamesha execute hota hai 

# try:
#     l=[1,2,3,4,5,6]
#     i=int(input("Enter the index"))
#     print(l[i])
# except:
#     print("Some error occurred")
# # finally bolta hai chaahe aap try me jaae ya execute me jaae me to run houga hui
# finally:
#     print("I will always run ") 

#main use
# agar function me return hoti value to function terminate but we use finally to 
# run some amount of code irrespectively wether we return value from try or except block

def func():
    try:
        l=[1,2,3,4,5,6]
        i=int(input("Enter the index"))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    # finally bolta hai chaahe aap try me jaae ya execute me jaae me to run houga hui
    finally:
        print("I will always run ") 


x=func()
print(x)