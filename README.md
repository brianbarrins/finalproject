# finalproject

# Author: Brian Barrins
# Student ID: G00299967
# Email: G00299967@GMIT.IE


______________________

#Purpose

The purpose of this assignment is to demonstrate the capabilities of a Caesar Cipher.
A Caesar Cipher, also known as a shift cipher, is an older form of "encryption" in which each letter in a text is shifted a number of places to the left or the right.
For example shifting <tt>"Hello there General Kenobi"</tt> by 2 characters to the right would result in the following message: <tt>"Jgnnq vjgtg Igpgtcn Mgpqdk"</tt>
In the above example each character is shifted to the right two spaces.

The code contained in the .py file in this folder is my attempt at making a Caesar Cipher.
______________________

#Code

The mathematical formula for a Caesar Cipher is displayed below:
<tt>newindex=(index - providedkey)%26</tt>
In this example the <tt>"newindex"</tt> is the position index of the to-be character.
This value is calculated by taking the original position index, subtracting the key (or shift) and then taking the modulus of that number with 26, as we are using 26 letters in our alphabet

Throughout the code there are multiple different outputs to the user. These are provided with granular details so as to give the user the ability to "see under the hood", but also help them to understand what the cipher is doing.
In the event of this actually being used, in a military Standard Operating procedures would be introduced and would need to be fool proof. Providing the user with updates as to each character being encoded/decoded or the full potential list of results could prove useful for any human error at either end of the transmission.

The nested if statements in the brute-force section of the code were introduced due to the logic of what I wanted to do.
In order to effectively use the list, to search for items in the dictionary, I had to find a method to split the individual words in the list, BUT still return the full list when getting the result.
The resulting code maintains the string, list and variable state required to achieve the intended output.
______________________

#Considerations

Additional considerations could and should be made for the following:
Efficiency of the code - the overall efficiency of the code
Number of nested ifs - could be reduced and a more effective method found should it exist
Variable names - could be shorted to help the code run faster
Usability - the overall appearance and effectiveness of the code for all demographics
______________________

#Next steps

In order to make the programme more complex, or to bring the program to life, I would create a number of additional functions depending on other cipher/encryption methods.
These functions would have the formulae to be used in the event of each of them being invoked.
The user would be initially welcomed and prompted as to whether they would like to "Encrypt" or "Decrypt" a message. After selection they would then be prompted to select the method by which to use.
These methods would change the code in line <tt>55-60, 106-111, 130-135</tt> and load in the capabilities of a different function.