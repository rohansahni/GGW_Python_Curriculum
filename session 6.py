# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:48:47 2019
Topic - Dictionary
By Dr. Sarvjeet Herald
@author: ACER
"""
# 1. Create a program to store student info - name, age , subject and marks
# Note for faculty - Some students may write a 2-D list. Please adapt accordingly.
'''
names = ["Sarvjeet", "Anmol", "Neha", "Rohan"]
age = [21, 16, 16, 21]
subject = ["computers", "computers", "computers", "computers" ]
marks = [90, 91, 92, 99]
'''
# Notable drawbacks
# 1. Seperate list for each item
# 2. Each list of same length
# 3. Information always stored at same index, each index refers to a different person

# 1.a Create a function to reterive Student information. Reterive course and marks of Sarvjeet
'''
def get_marks(student, name_list, age_list, subject_list, marks_list):
    i = name_list.index(student)
    age = age_list[i]
    subject = subject_list[i]
    marks = marks_list[i]
    return subject, marks
print(get_marks("Sarvjeet", names, age, subject, marks))
'''
# Notable Drawbacks
# messy if have a lot of different info	to keep track of
# must maintain many lists and	pass them as arguments	
# must always index using integers
# must remember to change multiple lists

# A better Way - Create a program to store student info - name, age , subject and marks 
# Notable Advantages
# One data structure
# index	item of interest directly (not always int)	
# but order cannot be guaranteed - Dictionay is unordered sequence similar to Sets
# Note for faculty - Show student Tabular representation of a list and a dictionary
'''
# 2. Create ampty dictionary
my_dictionary = {}

#3. Create dictionary of marks. Customize index by labels
marks = {"Sarvjeet":90, "Anmol":91, "Neha":92, "Rohan":99}  

# 3. Look up information by Key. 
# 3.a Print how much did Rohan Score 
print(marks["Rohan"])
# 3.a Print how much did Varun Score 
#print(marks['Varun']) #KeyError: 'Varun'
# 3.a Print how much did Sarvjeet Score 
print(marks["Sarvjeet"])

# 4. Delete Record for Sarvjeet
del marks["Sarvjeet"]

# 5. Delete the dictionary of marks 
del marks

#6. Alternative Approach - to use dictionary Constructor. 
# Create dictionar of marks again but using dictionary Constructor
marks = dict([("Sarvjeet", 90), ("Anmol", 91), ("Neha", 92),( "Rohan",99)])

# 7. Delete the dictionary of marks 
del marks

#7 Creation of disctionary of marks, when keys are strings - The thirds approach
marks = dict(Sarvjeet=90, Anmol=91, Neha=92,Rohan=99)
#Explain - Variable & Value, Same principlas of vaiable, multiple variables in Dict

# 8. Test using third approach- what if the names Sarvjeet, Anmo and so on are replaced by 1, 2, ..
#marks = dict(1=90, 2=91, 3=92,4=99)

# 9. Add marks of another student Varun to the Dictionary
marks["Varun"] = 95

#. 10 Create an English to Hindi Translation Dictionary. 
#. Ask user to input a word to translate and Print Response. Handle Response if the word is not present 
'''
'''
en_in = {"Hello":"Namaste", "Thank You": "Dhanyawaad", "Very Good":"Bahut Achay" }
word = input("Enter a word: ")

if word == "Hello":
    print(en_in["Hello"])
elif word == "Thank You":
    print(en_in["Thank You"])
elif word == "Very Good":
    print(en_in["Very Good"])
else:
    print("Sorry! I have not learned translation for this word.")

# ask student to extract two different words
    
# Mentor Note - Put it into function
    
'''

## ended session 5 here, given dictionary as homework
  
# 11. Convert a list into a dictionary
# Copy lists from Q1. names and age
'''

names = ["Sarvjeet", "Anmol", "Neha", "Rohan"]
age = [21, 16, 16, 21]
student_info_iterator = zip(names, age) # more than one list can be zipped
print(student_info_iterator) # this is a list iterator, which requires wrapping into a list
ages_list_pair = list(student_info_iterator) # This list of two tuples need to be wrapped in dict contructor
print(ages_list_pair)
age_dict = dict(ages_list_pair)
print(age_dict)

'''
'''
# 12. Efficient way to convert list into a dictionary
names = ["Sarvjeet", "Anmol", "Neha", "Rohan"]
age = [21, 16, 16, 21]
ages_dict_efficient = dict(zip(names, age))
print(ages_dict_efficient)

# 13. Add a new key pair to the newly converted dictionary e.g, Varun, 19 
ages_dict_efficient["Varun"] = 19
print(ages_dict_efficient)

# 14. Copy this dictionary to a new dictional student_info
student_info = ages_dict_efficient.copy()
# Please check ids of ages_dict_efficient and student_info    

#14. Alternate way to access item of dictionary. Get age of Varun
print(student_info.get("Varun"))

# 15. update age of Varun to 20
student_info["Varun"] = 20
print(student_info.get("Varun")) # No error if key does not exist 
# Go back to translator and apply get concept to see how would code change.


# 16. Print all key names in the dictionary, one by one
for i in student_info:
    print(i)
'''

'''
    
# 17. Print all Values in the dictonary, one by one
for i in student_info:
    print(student_info[i])

# 18. Alternative way to print values in dictionary, one by one
for i in student_info.values():
    print(i)

# 19. Print all key and Value Pairs in the dictionary, one by one
for index, i in student_info.items():
    print(index, i)
    
# 20. Determine if the specific key exists in the dictionary. Check for Jason
if "Jason" in student_info:
    print("Yes")
else: 
    print("No")
    
# Find number of items in the student info dictionary
print(len(student_info))

#21. Remove last inserted intem for the student info
print(student_info.popitem())
print(student_info)

#22. Remove Anmol from student info
print(student_info.pop("Anmol"))
print(student_info)

#23. Remove Jason from student info
#print(student_info.pop("Jason")) # KeyError: 'Jason'
print(student_info.pop("Jason", "None"))
print(student_info)

#24. Clear all items in student info
student_info.clear()
print(student_info)

#25. Create Nested dictionaries of three students - containing their name, age and marks
student_info = {
  "child1" : {
    "name" : "Sarvjeet",
    "age" : 21,
    "marks" :90
  },
  "child2" : {
    "name" : "Neha",
    "age" : 16,
    "marks" :92
  },
  "child3" : {
    "name" : "Rohan",
    "age" : 21,
    "marks" :99
  }
}
print(student_info)  

# 26. Print record of 1st student
print(student_info["child1"])

# 27. Print name of first student
print(student_info["child1"]["name"])

print(student_info.keys())

#28. Update nested dictionary with a new student, Anmol
child4 = {
  "name" : "Anmol",
  "age" : 16,
  "marks" :91
}

student_info.update({"child4":child4})
print(student_info)

#29. Analyze song lyrics. 
# a. Create a frequency dictorinay of words
# b. Find the words the occur the most
# c. Find the words the occur often X times. Value of X is entered by the user
# Note for faculty - From song dictionary, find most frequent word.	Delete most common word. Repeat.

# Use below Beatles Song as the data input
'''
'''
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]
'''

song='''she loves you yeah yeah 
yeah she loves you yeah yeah yeah
she loves you yeah yeah yeah

you think you’ve lost your love
well i saw her yesterday-yi-yay
it’s you she’s thinking of
and she told me what to say-yi-yay

she says she loves you
and you know that can’t be bad
yes she loves you
and you know you should be glad

she said you hurt her so
she almost lost her mind
and now she says she knows
you’re not the hurting kind

she says she loves you
and you know that can’t be bad
yes she loves you
and you know you should be glad

oo she loves you yeah yeah yeah
she loves you yeah yeah yeah
with a love like that
you know you should be glad

you know it’s up to you
i think it’s only fair
pride can hurt you too
pologize to her

Because she loves you
and you know that can’t be bad
Yes she loves you
and you know you should be glad

oo she loves you yeah yeah yeah
she loves you yeah yeah yeah
with a love like that
you know you should be glad
with a love like that
you know you should be glad
with a love like that
you know you should be glad
yeah yeah yeah
yeah yeah yeah yeah
'''

she_loves_you= song.split()
# Creating frequency Dictionary - Occurances of the word
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

beatles = lyrics_to_frequencies(she_loves_you)
print(beatles)

# b. Creating method to find words the occur the most
def most_common_words(freqs):
    #values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
common_words = most_common_words(beatles)
print(common_words)

# c. Creating method to find words the occur often X times

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict
        else:
            done = True
    return result
    
print("Words most often",words_often(beatles, 5))
'''
''' 
# 30. Given the following dictionary:
'''
 inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

Try to do the followings:

1. Add a key to inventory called 'pocket'.
2. Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
3. .sort()the items in the list stored under the 'backpack' key.
4. Then .remove('dagger') from the list of items stored under the 'backpack' key.
5. Add 50 to the number stored under the 'gold' key.
6. Print inventory
''' 
'''
inventory = {
     'gold' : 500,
     'pouch' : ['flint', 'twine', 'gemstone'],
     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket']=['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold']=inventory['gold']+50

print(inventory)

# 31. Create a new dictionary called prices. Follow the instruction below:
'''
'''
Create a Prices dictionary
Put these values in your prices dictionary:
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
Create a dictionary of stock
Put these values in your prices dictionary:
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    
Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
apple
price: 2
stock: 0

    
Let's determine how much money you would make if you sold all of your food.

    Create a variable called total and set it to zero.
    Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
    Finally, outside your loop, print total.

'''
'''
prices={}
#Add values
prices["banana"]=4
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3

#Create the stock dictionary
stock={}
#Add values
stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15

#Show all prices and stock
for food in prices:
    print(food, "Rs.", prices[food], "Items", stock[food])
    #print("price: ", prices[food])
    #print("stock: ", stock[food])
    
total=0
for price in prices:
    money= prices[price]*stock[price]
    print(money)
    total=total +money

print ("The total money is", total)
'''