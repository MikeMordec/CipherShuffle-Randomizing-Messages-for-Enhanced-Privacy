print ("Michael Mordec, 6/17/22, Lab 4, CSC 242:")
# cryptography ( shuffle elements in a list )

import random
# for random shuffle
 
strMsg = "The Courier is En Route with the Documents"
# the plaintext secret message
print (strMsg, "\n")

# convert the plaintext to lower case'
strMsg = strMsg.lower()
print (strMsg, "\n")

# replace any spaces in the message with an "x"
strMsg = strMsg.replace(" ","x")
print (strMsg, "\n")

plainTxtList = []
# declare a one - dimensional list

# populate the list with the characters comprising the message
for char in strMsg :
    # append the characters
    plainTxtList.append(char)
print(plainTxtList, "\n")

# declare the cipher list
scrambledList = []

# use list() to cast the plaintext list into the ciphertext list  
scrambledList = list(plainTxtList)

# randomly scramble the list of characters
random.shuffle(scrambledList)
print (scrambledList, "\n")

print("length of the scrambled list", len(scrambledList) ,"\n")
# determine the length of the list

# print in blocks of seven letters per row
for index in range(len(scrambledList)) :    
    print(scrambledList[index],end='')
    if(index % 7 == 6):
        print()

print ("\n", "\n") ; print ("\n", "\n")
#loop through every possible ordering of the leters
    #if the order contains all dictionary words than append to possible messages
    #after looped through all combinations left with all messages that could of been
    # all equally likely to be the message