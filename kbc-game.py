questions=["What is capital of India?\n1-Delhi\n2-Mumbai\n3-Kolkata\n4-Banglore",
           "Who is president of India?\n1-Draupadi Murmu\n2-M s Dhoni\n3-Narendra Modi\n4-Sharukh Khan",
           "How many states are there in India?\n1-34\n2-54\n3-55\n4-28",
           "Which continent does India belong?\n1-Middle east\n2-Antartica\n3-Asia\n4-Europe",
           "Which is neighbouring country on India among the given list?\n1-Bangladesh\n2-Japan\n3-Turkey\n4-Australia",]
correct_answers=[1,
         1,
         4,
         3,
         1]
user_score=0

for i in range(len(questions)-1):
    print("\n",questions[i])
    
    user_answer=int(input(("Enter your answer")))
    if user_answer==correct_answers[i]:
        print("Answer is correct")
        user_score=user_score+1
    else:
        print("Wrong answer")

Total_amount_won = user_score*1000
if user_score==0:
    print("\nSorry you won nothing ")
else:
     print("\nCongrats You won Rs",Total_amount_won)