# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:55:43 2019

@author: ACER
"""
#import counter class from collections library
from collections import Counter

# 1. Create Counter Object
cnt = Counter()

# 2. Create a list 
#    [1,2,3,4,1,2,6,7,3,8,1]

item_list = [1,2,3,4,1,2,6,7,3,8,1]

# 3. Create Dictionary of all the repetations
for item in item_list:
    cnt[item]+=1
print(cnt)


# 4. Better way - Create frequency dictionary of all items
item_list = [1,2,3,4,1,2,6,7,3,8,1]

# 5. pass item_list to the counter

cnt = Counter(item_list)
# 6. Check output of above in the variable explorer. #Above returns a fequency dictionary

#look at the key of the list and of the counter - any difference.
 
print(cnt[1]) # Repetations of same items in the list

# 7. Check repetations of other values 2,3,4,5,6,7,8
print(cnt[2]) 
print(cnt[5]) #return a zero count for missing items instead of raising a KeyError

# 8. Lets count frequency of words
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
    
#print frequency of red in the list
print("Red: ", cnt['red'])
print("Blue: ", cnt['blue'])
print("Green: ", cnt['green']) 

# 9. Check the coourances of words in a list
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

# Create frequency Dictionary for the Beatles Songs She loves you - Occurances of the word
cnt = Counter(she_loves_you)

'''
Mentor Note: Counter Result is an unordered collection where elements are stored as dictionary keys
and their counts are stored as dictionary values. Counts are allowed to be any integer value
'''

# 10. Counter with an inital value
#cnt = Counter('sarvjeet') # Check what happends, each word is assumed to be a key

# Check whether the name is of unique characters .. built on from the previous excerice.

name = Counter("Krish")
print('Name Values', name.values())
print(all(freq <= 1 for freq in name.values())) 
#Returns True if all elements of the iterable are true (or if the iterable is empty). 
#def all(iterable):
#    for element in iterable:
#        if not element:
#            return False
#    return True
############# ----------------Session 10 Ended here -----------------
# 11. Counter with an initial value - dictionary
c = Counter({'red': 4, 'blue': 2})  

# 12. Counter with an initial value - Keyword arguments
c = Counter(cats=4, dogs=8)

# 14. Sets count of cats to 5 
c['cats'] = 5

# 15. Adds key and the value of the key does not exist 
c['sausage'] = 0

# 16. Removes item Sausage
del c['sausage'] 

# 17. Return list of all the elements in the counter object
print(list(c.elements()))

# 18. Return the list of most common elements to the least
print(c.most_common())

# 19. Return the list of most two common elements
c['sausage'] = 0
print(c.most_common(2))

# 20. Beatles Songs She loves you. Find and Print the most common word in the song.
most_common_word = cnt.most_common(1)
print("Most common word in the song is \"", most_common_word[0][0],"\". It is repeated", most_common_word[0][1]," times")

#21. Suppose 2 cats and 3 dogs have been bought. Create a dictionary named bought for this. 
#    Subtract dictionary of bought with the origional list 
bought = Counter(cats=2, dogs=3)
c.subtract(bought)
print("Result of Subtraction", c)

# 22. Using update menthod, assign 2 cats, 5 sausages and 2 lions
c.update({'cats':2, 'sausage':5, 'lion': 2}) # Check if the Are values replaced or updated.
print(c)

'''
Working with Default Dictionary
'''
# 23. import defulatdict class from collections library
from collections import defaultdict

# 24. Create default dictionary
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])

# 25. Create a list of tuples consisting of colors. Using that create a disctionay of key and list of values 
s = [('color', 'blue'), ('color', 'orange'), ('color', 'yellow')]
d = defaultdict(list)
for k, v in s:
     d[k].append(v)
print("Line 184",d)
test = list(d.items())
print("line 185", test[0][0])

# ----------------Session 11 Ended here ----------------- Next Question given for home work to solve, please check
# 26. Do the same as above for fruits: banana orange banana. This time default dicitionary of set.s
s = [('fruit', 'banana'), ('fruit', 'orange'),('fruit','appke'), ('fruit','banana')]
d = defaultdict(set)
for k, v in s:
     d[k].add(v)
print(d)
for k, v in d.items():
    print('Line 182',k,',', v)
# 27. 

# 25. Create a list of tuples consisting of colors. Using that create a disctionay of key and list of values 
s = [('color', 'blue'), ('color', 'orange'), ('color', 'yellow'),('fruit', 'banana'), ('fruit', 'orange'),('fruit','banana')]
d = defaultdict(list)
for k, v in s:
     d[k].append(v)
print(d)

print("Testing List", list(d.items()))
test = list(d.items())
#print(test[0])
for k, v in d.items():
    print(k, ' ', v) #Specific Fruit
#for k, v in d.items():
#    print(k, ', '.join(v))
    
'''
Ordered Dictionary Starts here
'''
# 26. Create an ordered dictionary to store your roll numbers. 
#     Roll number and name can be passed as 2D list or a tuples wrapped in the list
#     Observe difference in the variable explorer and in the print output.
from collections import OrderedDict

roll_no = OrderedDict([
    [11, 'Sarvjeet'],
    [9, 'Anmol'],
    [17, 'Rohan'],
])

for key, value in roll_no.items():
    print(key, value)

# 27 Add a new entry Neha with roll number 10. Observe difference in the variable explorer and the print output. 
roll_no[10] = 'Neha'
for key, value in roll_no.items():
    print(key, value)

# 27 Delete record for roll number 9. Observe difference in the variable explorer and the print output.    
del roll_no[9]
for key, value in roll_no.items():
    print(key, value)

# 28 Add a new entry Neha with roll number 10. Observe difference in the variable explorer and the print output. 
roll_no[9] = 'Anmol'
for key, value in roll_no.items():
    print(key, value)
    
# ----------------Session 12 Ended here 
    
'''
Deque starts here
'''

# 29. Create a deque for the your name and print it.
from collections import deque
name = deque('Sarvjeet')
print('Deque       :', name)

# 30. Print length of deque
print('Queue Length:', len(name))

# 31. Count occurances of repeated word in a deque for example, ee is repeated 2 times in Sarvjeet 
print('Queue Count:', name.count('e')) #Count the number of deque elements equal to x.

# 32. Add intials of the last name e.g., H to the right of the queue
name.append('H') # Add x to the right side of the deque.
print('Deque with initials      :', name)
print('Printing only initials      :', name[-1]) # print only the intials

print('Left part   :', name[0])
print('Right part  :', name[-1])

# 33. Add title i.e., Dr. to the left of the deque
name.appendleft('Dr.') # Add x to the left side of the deque.
print('Deque with title     :', name)
print('Printing only title      :', name[0]) # print only the title

# 34. Remove last name initials from the deque
name.pop() #Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
print('Deque after pop     :', name)

# 35. Remove title from the deque
name.popleft() #Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
print('Deque after popleft     :', name)

# 36. Extend last name to the deque
name.extend('Herald') #Extend the right side of the deque by appending elements from the iterable argument.
print('Deque after extend     :', name)
 
# 37. Extend title at the start of the name
name.extendleft('Dr.') #Extend the right side of the deque by appending elements from the iterable argument.
print('Deque after extend left    :', name) # notice how is it being printed

# 38. Rotate the deque n steps to the right. 3 steps.
name.rotate(3) # Rotate the deque n steps to the right.
print("Print after rotate right: ", name)

# 39. Rotate the deque n steps to the left. 3 steps.
name.rotate(-3) # Rotate the deque n steps to the left.
print("Print after rotate left: ", name)

# 40. Remove the first occurance of e
print("Deque remove ", name.remove('e'))

'''
Named Tuple starts here
'''

# 41.Create a tuple with your first name, age and sex. Print it
rohan = ('Rohan', 25, 'M')  
print(name)

# Convert this record into a named tuple by assigning name to all the values

from collections import namedtuple
user = namedtuple('user', ' name age gender')
rohan = user(name='Rohan', age = 25, gender = 'M')
print("Rohan", rohan) # Print record
print ("Rohan's age", rohan[1]) # Print rohan's age

# Add user - Deepak 24 M
deepak = user(name='Deepak', age = 24, gender = 'M')
print(deepak)

# please carefully look at the variable explorer, especially the data types.

# In Later sessions please revisit and discuss reading data from excel to the named tuple and also from sqlite

#### Python Errors and Excception - New Topic
# 1. Syntax Errors
# while True print('Hello world') #SyntaxError: invalid syntax
''' 
Explanation: displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected.
The error is caused by (or at least detected at) the token preceding the arrow:
in the example, the error is detected at the function print(), since a colon (':') is missing before it. 
File name and line number are printed so you know where to look in case the input came from a script.
'''
'''
Exceptions Explanation:
Exceptions occur when exceptional situations occur in your program. 
For example, what if you are going to read a file and the file does not exist?
Or what if you accidentally deleted it when the program was running?
Such situations are handled using exceptions.
'''
# 2. Exceptions example
#age = int(input("Enter your age: ")) # Try input text. Check the error

#3. Handle exceptions using try..except. Value Error

'''
try:
    age = int(input("Enter your age: ")) 
except ValueError:
    print ("ValueError: could not convert string to integer")
else:
    print("Success, no error!")
    print("You entered: ", age)
'''

# Modify the above code and keep on asking the user to enter age 
# until the user enters the age in integer. Do it using function
# Why can you not use for and while loop instead of function.
'''
def input_age():
    try:
        age = int(input("Enter your age: ")) 
    except ValueError:
        print("ValueError: could not convert string to integer")
        input_age()
    else:
        print("Success, no error!")
        print("You entered: ", age)
input_age()

#4. try:  Assertaion Error
try:
    a = 100
    b = "Sarvjeet"
    assert a == b
except AssertionError:  
        print ("Assertion Exception Raised.")
else:  
    print ("Success, no error!")
'''    
#5. Key error in Dictionary
try:  
    a = {1:'a', 2:'b', 3:'c'}  
    print (a[4])  
except LookupError:  
    print ("Key Error Exception Raised.")
else:  
    print ("Success, no error!")
    
#6. Index Error
try:  
    a = ['a', 'b', 'c']  
    print (a[4])  
except LookupError:  
    print ("Index Error Exception Raised, list index out of range")
else:  
    print ("Success, no error!")

#7. Name Error
try:
    print (ans)
except NameError:  
    print ("NameError: name 'ans' is not defined")
else:  
    print ("Success, no error!")
    
# 8. Type Error
try:
    a = 5
    b = 6#"Sarvjeet"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
else:
    print ('Success, no error!')
finally:
    print("Thank you for your time") 
 

# Edit all your previous code - explorer, creator, inventor - to handle errors
    


 