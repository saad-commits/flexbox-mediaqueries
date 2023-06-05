# good morning sir 
# from datetime import datetime
# #print(time.gmtime(0))

# now =datetime.now()
# print("now: " , now)


# date_string = now.strftime("%d/%m/%y %H:%M:%S")
# print("date and time =",date_string)


import time
t=time.localtime()
print(t)
current_time = int(time.strftime("%H"))
print(current_time)
if(current_time < 12 ) :
    print("Good morning sir ")
elif(  current_time >=12 and current_time<=17 ):
    print("Good afternoon sir")
elif(  current_time >17 and current_time<=19 ):
    print("Good evening sir")
else:
    print("Good night sir")


    #code with harry
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
