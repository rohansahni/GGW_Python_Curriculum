# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:42:06 2019

@author: ACER
"""

#Create a set of fruits
fruits={"Apple", "Mango", "Guava", "Pineapple", "Banana"}
print(fruits)

# Edit the items in the set and introduce duplicates. Print.
# Are duplicates removed.
fruits = {"Apple", "Orange", "Apple", "Orange", "Banana"}
print(fruits)

# Add a new item to the fruits "Mango"
fruits.add("Mango")
print(fruits)

# Add multiple items to the set using updae method
#fruits.update("cherry", "grapes") Wrong approach
fruits.update(["cherry", "grapes"])
print(fruits)

# Claculate length of set
# Is it all or only unique fruits
print("Length of Set", len(fruits))

# Remove an item from set
fruits.remove("Banana")
print(fruits)

# Try the same operation again
# If the item to remove does not exist, what happens? It will raise an error.
#fruits.remove("Banana") #KeyError: 'Banana'
#print(fruits)

# Try to remove it using discard method()
fruits.discard("Banana") # This will not raise error if the item is not available.
print(fruits)

# Remove last item from the set of fruits
last_item = fruits.pop()
print(last_item)

#Does the above operation gaurantee that last item is always the one we think
# Sets are unordered, so when using the pop method, we will not know which item gets removed fro the set.

# Clear all items from the set
fruits.clear()
print("After clear method", fruits)

# Delete the set completely
fruits = {"Apple", "Orange", "Apple", "Orange", "Banana"}
del fruits
#print("After del method", fruits) #

# Test Membership of an item in fruits
fruits = {"Apple", "Orange", "Apple", "Orange", "Banana"}
print('orange' in fruits)
print('tomato' in fruits)

# Create set of vegetables
veg = {"Tomato", "Onion", "Lettuce"}

# Comment the above union. Create a new set of grocery containing both fruits and vegetables
# Is below operation supported
#grocery = fruits+veg 
#print("Grocery: ", grocery)
grocery = fruits.union(veg)
print("Grocery: ", grocery)

# What if requirement is to add vegetables to fruits
#print(id(fruits))
#fruits = fruits.union(veg)
#print(id(fruits))
#print("Fruits after union operation", fruits)

# A better way to update a set with items of an ohter set
fruits.update(veg)
print(" Update fruits with veg: ", fruits)


#Create two stringe using set constructor
a = "abcdefghabcdefgh"
b = "bdfhbdfh"
print("A: ", set(a))
print("B: ",set(b))

# Both union and update will exclude any duplicate items

# Write fruits using set function
# Does it Work? Check error
#fruits= set("Apple", "Mango", "Guava", "Pineapple", "Banana")
#print(fruits)

# Correct way
fruits= set(("Apple", "Mango", "Guava", "Pineapple", "Banana"))
print("Using set constructor", fruits)

#Copy set of fruits to a new set fruits2
fruits2 = fruits.copy()
print("Copied Set Fruits2: ", fruits2)

#Combine fruits and veg. Create a new set that contains items in fruits but not in veg
fruits.update(veg)
diff = fruits.difference(veg)
print("Difference: ", diff)

#Remove the items from fruits that also exist in veg
fruits.difference_update(veg)
print("Differene update: ", fruits)
print("Differene update: ", veg)

#Combine fruits and veg. Return the items that exist in fruits and veg
fruits.update(veg)
print("Intersection", fruits)
print("Intersection", veg)
diff = fruits.intersection(veg)
print("Intersection: ", diff)

#Combine fruits and veg. Removes items that are not present in both fruits and veg
fruits.update(veg)
fruits.intersection_update(veg)
print("Intersection Update: ", fruits)

#Create set of 5 fruits. Create set of 5 electronic devices. Validate if two sets contain any smae items
fruits = {"Apple", "Orange", "Apple", "Orange", "Banana"}
elec = {"Mobile", "Laptop", "Desktop"}
test = fruits.isdisjoint(elec)
print("Disjoint Test: ", test)

# Combine fruits and veg. Check if veg is present in fruits
fruits.update(veg)
test = veg.issubset(fruits)
print("Subset Test: ", test)


#Validate if fruits is a superset of veg (if all the items of veg are in fruits)
print("Superset Test: ", fruits.issuperset(veg))

#Return set that contain all items from fruit and veg, but are not present in both the sets
sym_diff = fruits.symmetric_difference(veg)
print("Symetric Difference: ", sym_diff )

# Remove the items that are present in both the sets, and insert items that are not present in both the sets
print("Symetric Difference Update - Fruits: ", fruits )
veg2 = {"Tomato", "Onion", "Lettuce", "Carrot", "Dream"}
print("Symetric Difference Update - Veg: ", veg2 )
fruits.symmetric_difference_update(veg2)
print("Symetric Difference Update: ", fruits )


#Identify letters that arre in a but not in b
print(set(a)-set(b))

#Identify all unique letters in a and b
print(set(a) or set(b))

#Identify letters present in a that are also present in b
print(set(a) and set(b))

# Identify letters in a and b, both do not include those that are present in both
print(set(a) ^ set(b))

# Write code to access and print each item in the fruits set using using for loops
for fruit in fruits:
    print(fruit)
    
#*********** Set Excercises ****************************
# 1. Create a function to validate whether the test string has unique characters.
# Ask user to input a string

def are_string_chars_unique(test_string):
    chars_set = set() 
    for char in test_string:     
        if char in chars_set:
            return False
        else:
            chars_set.add(char)
    return True

user_input = input("Enter a name or a word: ")
print(are_string_chars_unique(user_input))


# 2. Create two sets
# a = {65, 42, 78, 83, 23, 57, 29}
# b = {67, 73, 43, 48, 83, 57, 29}

#2. Find the intersection and remove those elements from the first set
a = {23, 42, 65, 57, 78, 83, 29}
b = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", a)
print("Second Set ", b)

intersection = a.intersection(b)
print("Intersection is ", intersection)
for item in intersection:
  a.remove(item)

#a.difference_update(b) alternative way without for loop

print("First Set after removing common element ", a)

# 3. Given two sets, Checks if One Set is Subset or superset of Another Set. 
# if the subset is found delete all elements from that set
# a = {27, 43, 34}
# b = {34, 93, 22, 27, 43, 53, 48}
a  = {57, 83, 29}
b = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", a)
print("Second Set ", b)

print("First set is subset of second set -", a.issubset(b))
print("Second set is subset of First set - ",b.issubset(a))

print("First set is Super set of second set - ", a.issuperset(b))
print("Second set is Super set of First set - ", b.issuperset(a))

if(a.issubset(b)):
  a.clear()
  
if(b.issubset(a)):
  b.clear()

print("First Set ", a)
print("Second Set ", b)
