# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:01:14 2019

@author: ACER
"""

# 1. Create a empty tuple
fruits = ()
print(fruits)

#2. Create tuple of 5 fruits
fruits = ("Apple", "Mango", "Guava", "Pineapple", "Banana")
print(fruits)

#3. Aleternative way of creating tuple of 5 fruits without paranthesis
fruits = "Apple", "Mango", "Guava", "Pineapple", "Banana", "Apple"
print(fruits)

#4. Print the first and the fourth element of the tuple of fruits. 
print(fruits[0], "and", fruits[3])

#5. Create a new tuple of Grofer’s grocery with an single item called fruit.
grocery = ("fruit") # This is stored as string not a tuple
print(grocery)

grocery = ("fruit",) # This is a tuple fo single item. Caution! Comma at the end is required.
print(grocery)

#6. Create a new tuple of recent fruit arrivals. Concatenate this new tuple and fruits  
new_arrivals = "Strawberry", "Grapes", "Orange"
print(fruits+new_arrivals)

#7. Store the result of concatenation into all fruits.
#Print & Check memory address of fruits, new arrivals and all fruits. Are these same?
all_fruits = fruits+new_arrivals
print(id(fruits), id(new_arrivals), id(all_fruits))

#8. Repeat the grocery tuple 5 times. 
print(grocery*5)

#9. Create a list of same 5 fruits. Modify the first item of the list to “berries”.
#Now do the same modification to the tuple of fruits. Is tuples mutable?
fruits_list = ["Apple", "Mango", "Guava", "Pineapple", "Banana"]
fruits_list[0]= "Berries" #uncomment below line to make this excercise work
#fruits[0] = "Berries"  #This is error prone. TypeError: 'tuple' object does not support item assignment

#10. Delete a specific fruit from the list. Try the same for a specific fruit from the new arrivals. 
del fruits_list[4]  #uncomment the line below for this excercise
#del new_arrivals[2]
print(new_arrivals)

#11. Delete the grocery tuple.
del grocery

#12. Find the length of fruits tuple
print("Length of fruits tuple: ",len(fruits))

#13. Convert list of fruits to tuple.
print(tuple(fruits_list))

#14. Using For loops iterate and print each item of fruits tuple 
for i in range(len(fruits)): 
    print("Item",i, ": ",fruits[i]) 

#15. Create a new, nested tuple of fruits and  recent fruit arrivals. Print it.
grocery = fruits, new_arrivals   
print(grocery)

#16. Extend last question to iterate and print each element of grocery along with their indexes.
print("\nSolution of Question 16")
for row_index,value_row_item in enumerate(grocery):
    for col_index, value_cell_item in enumerate(value_row_item):
        print (row_index,",", col_index,": ", value_cell_item, sep="")
        
#17. Ask name of the fruit from the user and check if it exists in grocery.      
# Please uncomment below for the solution
'''
print("\nSolution of Question 16")
search_term =  input("Enter name of the fruit you wish to search: ")
for row_index,value_row_item in enumerate(grocery):
    for col_index, value_cell_item in enumerate(value_row_item):
        if search_term == value_cell_item:
            print("Yes, Item ",search_term, " exists in the grocery tuple at cell index ", row_index,",", col_index, sep="")
        else: 
            print("Sorry your search term",search_term, "does not exist")
'''

#18. Control the output so that if there are multiple copies of the user search fruit item exists 
# or not exists in the tuple, the output is displayed only once but with all the cell indexes
# at which it is located.
search_result = [] # Discuss what would happen if this is a tuple, will it work
print("\nSolution of Question 16")
search_term =  input("Enter name of the fruit you wish to search: ")
for row_index,value_row_item in enumerate(grocery):
    for col_index, value_cell_item in enumerate(value_row_item):
        if search_term == value_cell_item:
            search_result.append([row_index, col_index]) # Discuss what would happen if this is a tuple, will it work
if len(search_result) ==1:   
    print("Yes, Item ",search_term, " exists in the grocery tuple at cell index ", row_index,",", search_result[0][0], search_result[0][1],sep="")
elif len(search_result)>1:
    print("Yes, Item ",search_term, " exists in the grocery tuple. These are located at cell indexes ")
    print(search_result)
else:
    print("Sorry your search term",search_term, "does not exist")
    
#19. Quizz students which the prospective errors and ask them to fix code.    
