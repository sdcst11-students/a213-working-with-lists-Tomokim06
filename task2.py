#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

list = []

q1 = "Enter a word to put on the list: "
a1 = str(input(q1))
q2 = "Enter a word to put on the list: "
a2 = str(input(q2))
q3 = "Enter a word to put on the list: "
a3 = str(input(q3))
q4 = "Enter a word to put on the list: "
a4 = str(input(q4))
q5 = "Enter a word to put on the list: "
a5 = str(input(q5))



list.append (a1)
list.append (a2)
list.append (a3)
list.append (a4)
list.append (a5)
print(list)
