# for i in range(14):
#     if(i==10):
#         print("skip the whole loop  ")
#         break
#     print("5 X",i+1,"=",5*(i+1))
# # break ka matlab loop ko chodke nikal jaao
# # continue matlab iteration ko chodke nikal jao
# for i in range(14):
#     if(i==10):
#         print("skip the value for 10")
#         continue
#     print("5 X",i+1,"=",5*(i+1))


# emulate do while loop 
i=0
while True:
    print(i)
    i= i+1
    if(i%100==0):
        break