#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

#import relevant items for use
from typing import final
import pandas as pd
import string
import csv
import random

#setup logging
import logging

logging.basicConfig(filename='./caesarcipher.log', #create logging file
    filemode ='a',
    level=logging.INFO,
    format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s - line: %(lineno)d ')


alphabet =string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz" #create alphabet of letters for use
dictionary = pd.read_csv('./words.csv')#read in common words as variable


#function for enciphering
def encipher():
#print welcome and instructions
    print ("Hello General! \nEnter your message to the frontlines")
    originalmsg = input("When finished, please click Enter to confirm \n\n")#take input for message
    providedkey=input("\nPlease specify a key?\nFor random key, please leave blank....")#take input for key
    

    try:
        # Convert it into integer
        providedkey = int(providedkey)
        print("\nInputted key is an integer number", providedkey) #provide user feedback
        logging.info("User input is correct and being used")
    except ValueError: #value error if not an integer and unlikely a float or decimal
        try:
            providedkey = float(providedkey) # Convert it into float
            providedkey=int(round(providedkey)) #round the number so it can be a usable integer
            print("\nInputted key was a float  number. Number is now an integer of value = ", providedkey) #provide user feedback
            logging.info("User input is float and being rounded to be used")
        except ValueError: #if it is still a value error, then they entered text
            #else create random key to be used
            print("\nNo key specified, a random key will be used")
            providedkey=random.randint(1,26) #provide a random integer
            print("\nInputted key was not a number. The random number to be used is = ", providedkey) #provide user feedback
            logging.info("User input is incorrect and being assigned a random number")
    
    #code for if is integer
    if type(providedkey)==int:
        providedkey=providedkey #keep key the same
        encipheredmsg="" #initialise string
        for c in originalmsg: #begin first loop for each character in the alphabet
            index = alphabet.find(c) #find originalmsg position
            if c in alphabet: #if character in the alphabet
                newindex=(index - providedkey)%26 #give the position a new position by shifting left with the key
                newc = alphabet[newindex] #create new character
                encipheredmsg+=newc #add new character to string
                
            else:
                encipheredmsg=encipheredmsg+c #if character not in alphabet e.g. spaces, commas, special characters then add them as they are
    #can remove as technically redundant due to error catching above. However including for resilience
    else:
        providedkey=random.randint(1,26) #make random key
        for c in originalmsg:#begin first loop for each character in the alphabet
            index = alphabet.find(c) #find originalmsg position
            if c in alphabet: #if character in the alphabet
                newindex=(index - providedkey)%26 #give the position a new position by shifting left with the key
                newc = alphabet[newindex] #create new character
                encipheredmsg+=newc #add new character to string
            else:
                encipheredmsg+=c #if character not in alphabet e.g. spaces, commas, special characters then add them as they are
                
    print("\nEncoding: '",originalmsg,"' with a key: ",providedkey) #print out the narration to the user
    print("\nYour message to send is: '",encipheredmsg,"'")  #print out the enciphered message

#function for decciphering  
def decipher():
    print ("Hello Major! \nDo you have a new message from command?")
    msgtodecode = input("Enter your message from command in order to deccipher it: \n") #take input for message
    givenkey=input("\nDo you possess a key for decoding? Y or N\nIf Y, enter the key: ") #take input for key
    

    try:
        # Convert it into integer
        givenkey = int(givenkey)
        print("\nKey to be used is an integer number", givenkey) #provide user feedback
        logging.info("User input is correct and being used")
    except ValueError: #value error if not an integer and unlikely a float or decimal
        try:
            givenkey = float(givenkey)# Convert it into float
            givenkey=int(round(givenkey)) #round the number so it can be a usable integer
            print("\nKey to be used was a float  number. Number is now an integer of value = ", givenkey)
            logging.info("User input is float and being rounded to be used")
        except ValueError:
            print("\nNo key specified, a random key will be used")
            logging.info("User input is incorrect and brute force will be used")
            
    #code for if is integer        
    if type(givenkey) == int:
        givenkey=givenkey #keep key the same
        decipheredmsg="" #initialise string
        logging.info("Known key is being used tp decipher")
        for c in msgtodecode: #begin first loop for each character in the the message
            index = alphabet.find(c) #find originalmsg position
            if c in alphabet: #if character in the alphabet
                newindex=(index + givenkey)%26 #give the position a new position by shifting left (inverted for formula) with the key
                newc = alphabet[newindex] #create new character
                decipheredmsg+=newc #add new character to string
               
            else:
                newc=c #store character so skip doesn't occur
                decipheredmsg=decipheredmsg+c #if character not in alphabet e.g. spaces, commas, special characters then add them as they are
            print("Decoding: the character",c, " as: ",newc) #provide the user with some live feedback for entertainment
        print("\nYour message states: ",decipheredmsg) #show user the answer
    #if the user did not enter a key, then we will automatically decipher the message    
    else:
        print("\nLooks like you don't have a key! Guess we'll have to crack that for you!")
        logging.info("Brute force is about to begin")
        givenkey=0 #assign zero to start
        decipheredformats= [] #initialise
        decipheredlist=[]#initialise
        
        while givenkey< len(alphabet):#while loop to keep key within range
            decipheredmsg=""#initialise
            msgtodecode=msgtodecode.lower()#convert message to lower to match the dictionary
            
            for c in msgtodecode: #begin first loop for each character in the alphabet
                if c in alphabet: #if character in the alphabet
                    index=alphabet.find(c) #find the index
                    newindex=(index+givenkey)%26 #make the new index
                    newc=alphabet[newindex] #create the new character based on new index
                    decipheredmsg+=newc #add character to message
                    
                else:
                    decipheredmsg+=c #add character as is
            print("Decoding: ",msgtodecode,"with a key of: ",givenkey," results in: ",decipheredmsg) #provides running commentatry for feedback and entertainment
            #print("Your decoded message states: ",decipheredmsg)
             
            decipheredformats.append((givenkey,decipheredmsg)) #append the list with the key and deciphered message
            decipheredlist.append(decipheredmsg) #append just the decciphered message
            givenkey=givenkey+1 #increment key by 1 and repeat loop
        

    #determine the most likely match to ease the brain power required to decipher
        results=[] #initialise
        pureword=[] #initialise
        finalmessage=[] #initialise
        pureword=[words for segments in decipheredlist for words in segments.split()] #split the words which we decciphered into individual words for searching and matching
        #print(pureword)
        with open('words.csv') as words, open('out.csv','w') as output: #open the csv file (containing the words)
            reader = csv.reader(words) #store the words as a variable
            finalmsg = csv.writer(output) #write final message to a csv file
            #nested for loops
            for row in reader: #for each row in the dictionary of words
                for x in pureword: #for each word in the purewords list
                    if x in row: #if the word is in the row
                        print('Found the word: ',x) #show word for feedback
                        results.append(x) #store word
            print("Your message may contain the following key-words: ",results) #provide user feedback with possible matches
            logging.info("Key words are produced")
            #second loop to tie the word back to the deciphered phrase
            for row in decipheredlist: #for each row in the decipheredlist (just the message (no key))
                for x in results: #for each potential word found so far
                    if x in row: #if the potential word is found in the decipheredlist
                        finalmessage.append(row) #add that output to a final message
            logging.info("Key phrases are produced")            
            from collections import Counter #import counter so we can sort based on popularity
            finalmessage=Counter(finalmessage).most_common() #sort the most common
            finalmessage=[i[0]for i in finalmessage] #loop for all the matches
            print("The potential matches that have been found are: ",finalmessage) #show the potential matches
            print ("The most likely decciphering is as follows: ",finalmessage[0]) #show the most matched phrase
            logging.info("Deciphering complete")

    
encipher() #run encipher
deccipher() #run decipher
