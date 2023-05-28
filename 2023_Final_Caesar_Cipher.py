from Final_Cipher_art import logo

import os 


#The alphabet list is Doubled to Account for if the user enters 'Z' and tries to shift forward - You won't be able to since there would be nowhere to go past 'Z'


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


"""
Clear function clears the screen for the user after restarting the program
"""
def clear():
    os.system('clear')


def cipher_text(text_input,shift_amount,question_input):
    """
    This function takes 3 inputs 
    
    1) text_input-Takes the message you want to encode/decode 
    
    2) shift_amount- Takes the number of places you want to shift each character within the alphabet list backwards or forward
    
    3) question_input-Takes the input of if you want to encode a message or decode a message. Encoding moves forward in the alphabet. Decoding moves backwards in the list by multiplying
    the shift amount by -1 to make the number negative.
      
    This function works by using the index method. It checks every character you've typed as your message and finds it's corresponding index position number within the alphabet list.

    It then adds or subtracts that index position number by the shift_amount you've entered, this new number is now the new index postion number which is a letter in the alphabet list

    Finally all characters are added to the variable final_text and is then printed for the user to see


    """
    
    final_text=""
    if question_input=="decode":
        shift_amount*=-1
    for char in text_input:
        if char in alphabet:
        
            typed_letter=alphabet.index(char)
        
            new_index_position=typed_letter+shift_amount
        
            new_letter=alphabet[new_index_position]

            final_text+=new_letter
        else:
            final_text+=char

    print(f"Here's the {question_input}d result: {final_text}")

done_coding=False


while done_coding==False:
    print(logo)
    question=input("Type 'encode' or 'decode': ")

    text=input("Type the message you want to encode or decode: ")

    shift=int(input("What is the shift number?: "))

    shift=shift % 26
    
    #I've used the modulo operator to get the remainder of the division of what is entered as the shift amount.
    
    #If someone were to enter a shift number larger than 26 (There are 26 letters in the alphabet) coupled with characters that are towards the end of the alphabet you'd get an index error
    
    #so essentially what this modulo operator does is allow you to enter any number and it will loop back to the begining of the list
    
    #For example: if I type 'a' as my message and my shift number is 27 my output will be 'b' That's because the letter 'a' is index postion 0, 'z' is index postion 25 so then it loops back to 'a' then 'b' which is 27 places  """



    cipher_text(text_input=text,shift_amount=shift,question_input=question)

    if input("Type 'yes' if you want to go again. Otherwise type 'no': ")=="yes":
        clear()
        cipher_text(text_input=text,shift_amount=shift,question_input=question)
    else:
        done_coding=True
        print("Goodbye")



