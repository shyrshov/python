# Task 1: Set Creation and Elements
# Create a set named my_set that contains the following elements: 1, 2, 3, 4, 5. Print the set.

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Task 2: Set Operations
# Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, perform the following set operations and print the results:

# Union: Combine the elements from both sets without duplicates.
# Intersection: Find the common elements between the two sets.
# Difference: Find the elements that are in set1 but not in set2.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)
print(set1.intersection(set2))
print(set1.difference(set2))

# Task 3: Set Membership
# Given a set my_set = {1, 2, 3, 4, 5}, check if the value 3 is present in the set. Print True if it is, and False otherwise.

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

# Task 4: Set Length
# Given a set my_set = {"apple", "banana", "cherry", "durian"}, print the number of elements in the set.

my_set = {"apple", "banana", "cherry", "durian"}
print(len(my_set))

# Task 5: Set Addition and Removal
# Given an empty set my_set, perform the following operations and print the resulting set after each step:

# Add the element "apple" to the set.
# Add the elements "banana" and "cherry" to the set.
# Remove the element "apple" from the set.

my_set = set()
my_set.add('apple')
print(my_set)
my_set.update({'banana', 'cherry'})
print(my_set)
my_set.remove('apple')
print(my_set)

# Task 6: Set Intersection Update
# Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6},
# use the appropriate set method to update set1 with the elements that are common between set1 and set2. Print the updated set1.

set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
set1.update(set1.intersection(set2))
print(set1)

# Task 7: Set Symmetric Difference
# Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, calculate and print the symmetric difference between the two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.symmetric_difference(set2))

# Task 8: Set Subset Check
# Given two sets set1 = {1, 2, 3} and set2 = {1, 2, 3, 4, 5}, check if set1 is a subset of set2. Print True if it is, and False otherwise.

set1 = {1, 2, 3} 
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))

# Task 9: Set FrozenSet
# Explain the concept of a frozen set in Python and discuss its characteristics and use cases.

# Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the 
# frozen set remain the same after creation. Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.

# Task 10: Set Conversion
# Given a list my_list = [1, 2, 3, 4, 5], convert it into a set named my_set. Print the resulting set.

my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)