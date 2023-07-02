# Task 1: Tuple Indexing
# Given a tuple my_tuple = (1, 2, 3, 4, 5), access and print the third element.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])

# Task 2: Tuple Slicing
# Given a tuple my_tuple = (1, 2, 3, 4, 5), create a new tuple that contains only the elements from index 2 to index 4 (inclusive).
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[2:5]
print(new_tuple)

# Task 3: Tuple Concatenation
# Given two tuples tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6), create a new tuple that is the concatenation of both tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# Task 4: Tuple Unpacking
# Given the tuple my_tuple = ("John", 25, "USA"), unpack the elements into three separate variables named name, age, and country. Then, print the values of these variables.
my_tuple = ("John", 25, "USA")
name, age, country = my_tuple
print(name, age, country)

# Task 5: Tuple Membership
# Given a tuple my_tuple = (1, 2, 3, 4, 5), check if the value 3 is present in the tuple. Print True if it is, and False otherwise.
my_tuple = (1, 2, 3, 4, 5)
if 3 in my_tuple:
    print(True)
else:
    print(False)

# Task 6: Tuple Length
# Given a tuple my_tuple = ("apple", "banana", "cherry", "durian"), print the number of elements in the tuple.
my_tuple = ("apple", "banana", "cherry", "durian")
print(len(my_tuple))

# Task 7: Tuple Reversal
# Given a tuple my_tuple = (1, 2, 3, 4, 5), create a new tuple that contains the elements in reverse order.
my_tuple = (1, 2, 3, 4, 5)
new_tuple =my_tuple[::-1]
print(new_tuple)

# Task 8: Tuple Packing
# Create a tuple named person that contains the following information: the name "Alice", the age 28, and the country "Canada". Print the tuple.
person=('Alice', 28, 'Canada')
print(person)

# Task 9: Tuple Immutability
# Explain the concept of immutability in Python tuples and provide an example that demonstrates the immutability of tuples.
"Immutable objects can't be changed, so the tuple can't be changed after it was created"
# tuple = (1, 2, 3)
# tuple[1] = 5 - this will cause an error

# Task 10: Tuple Conversion
# Given a list my_list = [1, 2, 3, 4, 5], convert it into a tuple named my_tuple. Print the resulting tuple.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)