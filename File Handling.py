# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:16:50 2019

@author: ACER
"""

# 1. Open a new file in a write mode. Check this in your directory
#f = open("output", "w")

# 2. Open a new text file in a write mode. Check this in your directory
#f = open("output.txt", "w")

# 3.  What are the other popular file extensions. Create a file with these extensions.

'''
4. File could be opened in 
1. write-only mode ("w")
2. read-only mode ("r") #by default file is opended in read only
3. Read and Write mode ("r+")
4. Append mode ("a"). It adds any new data you write to the file to the end of the file
5. Append + read mode
6. Binary is added to Mode ("mb"). Data is read and written in the form of bytes objects. Used for all files that don’t contain text.
'''

# 5. Write Data on a text file
#f = open("output.txt", "w")
#f.write("My name is Dr. Sarvjeet Herald") 

# 6. Try to Delete this file in the file explorer. Will it delete

# 7. Close the file so allow deletion or release of resources. Otherwise you may face problem reading and writing 
#f.close()

# 8. Create a list to record squared number from 1 to 10. 
#    Store the results into a new file. Make sure each number is stored in a new line.
#    Open file in the file explorer and check the content 

my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "w")
for num in my_list:
    data=str(num)  # other types of objects need to be converted into a string before they can be stored
    my_file.write(data)
    my_file.write("\n")
my_file.close() 

# 9 . Read the file you have just created and print the content in the Python
my_file = open("output.txt", "r")
print(my_file.read())
my_file.close()

# 10 . Read the file you have just created but one line at a time
my_file = open("output.txt", "r")
print(my_file.readline())
print(my_file.readline())
my_file.close()

#use readlines() to get list
# 11. Create a new file lines.txt from the file explorer with the following content
'''
    I am the first line
    I am the second line
    I am the thrid line
'''
#   Read all the line of the file using for loop
my_file = open("lines.txt", "r")
for line in my_file:
    print(line)
my_file.close()


# 12. Another way to read content
#     with keyword
#     file is properly closed after its suite finishes, even if an exception is raised at some point. 
#     Using with is also much shorter than writing equivalent try-finally blocks

with open('output.txt') as f:
    read_data = f.read()    # please check data type of read_data
print(f.closed)

# 13. Read a char from the file. Give position of the char 
my_file = open("lines.txt", "r")
print(my_file.read(1))

#14. Check the file name
print(my_file.name)

#15. Check the file mode
print(my_file.mode)

#16. Current offset of the file pointer in a file.
print(my_file.tell())

# 17. change the position of a file pointer in a file. Check the changed pointer
my_file.seek(4)
print(my_file.tell())


# do the excerice for append to lists
# 18 Remane file
import os
#os.rename("linename.txt", "newlinename.txt") #file needs to be closed

# 19. Delete file
#os.remove("newlinename.txt")
 

''' 20. names.txt has a list of a bunch of names
Count how many of each name there are in the file, and print out the results to the screen
'''
from collections import defaultdict
count=defaultdict(int)
filename = "names.txt"
with open(filename, 'r') as open_file:
    entry = open_file.readline()
    while entry:
        count[entry.strip()]+=1
        entry = open_file.readline()
        
print(count)

for i in count.keys():
    print(i, count[i])




''' 20. Scene Recognition Database from MIT
Lists the file directory hierarchy for the images 
Look at few lines of file to find which part represents the scene category. 
Read the file. Extract unique categories and how many file in each category. 
Which concepts will you use - Read file and dictionary
'''
#----- Session 14 ended here
'''
Majority of Data on world wide web is in unstructured form such as in the given project-data.txt
 
Text file contains thousands of words. 
Many words share almost the same meaning. 
Each word had its definition and an example sentence next to it.
There are spaces and newlines between a word and its sentence
Some aspects were missing from the words. 
But all this is recorded in an unorganised manner.
e.g. Glower is preceded by a newline whereas others are not.
     Shirk is preceded by a newline

Preprocess Data of the file and give it a neat and clean structure. 
Neatly assort all similar meaning words beside a topic

Store the structure data into a CSV file which can also be opened in excel. 
Eventual csv file that you create when imported into excel will have 1870 rows + header.
  
File open parameters
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
buffering (optional) - used for setting buffering policy
encoding (optional) - name of the encoding to encode or decode the file
errors (optional) - string specifying how to handle encoding/decoding errors
newline​ (optional) - how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'
closefd (optional) - must be True (default) if given otherwise an exception will be raised
opener (optional) - a custom opener; must return an open file descriptor

Steps to solve
1. Forming a Regex to match a number and the word next to it
    numRegex = re.compile(r'(\d)(\d*)?(\.)(\s*)?(\w*)')
    sequence of characters that forms a search pattern.
    Regex functions
    findall	Returns a list containing all matches
    search	Returns a Match object if there is a match anywhere in the string
    split	Returns a list where the string has been split at each match
    sub	Replaces one or many matches with a string
2. Obtaining a list of lines as strings from the text file
3. Extracting words, meanings, and example sentences separately and adding them to corresponding lists
4. Creating values for keys using Zip Function and Parameter Unpacking
5. Assigning values to the keys in the dictionary

'''
import re
'''
file = open('project-data.txt','r',errors = 'replace')
numRegex = re.compile(r'(\d)(\d*)?(\.)(\s*)?(\w*)')
'''
# Regex to match word number and word itself (Eg. 1. Angry)
numRegex = re.compile(r'\d')
#numRegex = re.compile(r'(\w*)?(\.)(\s*)?(\w*)')
x = numRegex.findall(1, 1)
print(x)

'''
matched_strings_list = []
for groups in numRegex.findall(file.read()):
    item = ''.join(groups)
    clean_item = item.replace('\n','')
    matched_strings_list.append(clean_item)
    
file.close()
'''
