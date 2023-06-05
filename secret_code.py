#write a secret language code 

#codng rules- 
# if the word contiains atleast 3 characters , remove the first letter append to last and finall
# add 3 random characters at the start and at the end
# else if less than 3 charcters word
# simply reverse it
import random
import string
import sys




def encoder(a):
 
 input_list=a.split(" ")
 final_encoded_string=""
 for i in range(len(input_list)):
    if( len(input_list[i]) >2 ):
        
      word=input_list[i]
      
      # first_character=word[0]
      # new_word = word.replace(word[0],"")
      # new_word += first_character

      # next line is shortcut of whole three lines above 

      new_word = word[1:] + word[0]
    
    #   for i in range(len(word)):
       
    #    word[i]=word[i+1]   # we cant use this as strinfg are immutable
    
      start_string= "".join(random.choices(string.ascii_letters ,k=3))
      end_string= "".join(random.choices(string.ascii_letters ,k=3))
      new_word = start_string + new_word + end_string+" "
      final_encoded_string +=new_word

    else:
       word=input_list[i]
       new_word = word[::-1]
       final_encoded_string +=new_word +" "
  
 return final_encoded_string



def decoder(a):
  input_list=a.split(" ")
  final_decoded_string=""
  for i in range(len(input_list)):
    
    if (len(input_list[i])>2):
      word=input_list[i]
      new_word=word[3:-3] 
      last_character=new_word[len(new_word)-1]
      new_word=new_word.replace(new_word[len(new_word)-1],"")
      new_word=last_character+new_word
      final_decoded_string += new_word + " "
 
    else:
      word=input_list[i]
      new_word=word[::-1]
      final_decoded_string += new_word + " "
  return final_decoded_string
      
input_string = input("enter the message you want to encode biatch \n")
encoded_string = encoder(input_string)
decoded_string=decoder(encoded_string)

# print("The input string is --->",input_string)              
# print("after encoding the string is --->",encoded_string)              
# print("after decoding the string is --->",decoded_string)              
        
# Please help me understand if this can further shortened:
# # Secret language
# import random
# code_decode = input("Would you like to 'code' or 'decode' a message: ")
# msg = input(f"Please input the message to be {code_decode.lower()}d: ").split()
# msgn=[]
# abcd = "quickbrownfoxjumpsoverthelazydog"
# for word in msg:
#   if code_decode.lower() == "code" and len(word)>=3:
#       word= word[1:] + word[0]
#       for i in range(3):
#         word = abcd[random.randrange(len(abcd))] + word + abcd[random.randrange(len(abcd))]
#       msgn.append(word)
#   elif code_decode.lower() == "decode" and len(word)>=3:
#       word = word[3:-3]
#       word= word[-1] + word[:-1]
#       msgn.append(word)
#   else: msgn.append(word[::-1])

# msgnstr = ' '.join([str(elem) for elem in msgn])
# print(msgnstr)