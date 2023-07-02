# Lists:

# Task 1: Create a new list with numbers between 100 and 200 that can be devided by 3.
list = [x for x in range (100, 200) if x % 3 ==0]
print(list)

# Task 2: Given a list [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]. Find the maximum and minumum numbers in this list.
list = [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]
print(max(list))
print(min(list))

# Task 3: Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Reverse this list in place without creation a new list. Print the result to the console.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.reverse()
print(list)

# Task 4: Given a list with duplicates [1, 2, 3, 4, 3, 1, 5, 2, 6]. You need to create a new list with all the duplicate elements removed. The order of the elements should be preserved. For example, if the input list is [1, 2, 2, 3, 4, 1, 5], result will be [1, 2, 3, 4, 5].
list = [1, 2, 3, 4, 3, 1, 5, 2, 6]
withoutDuplicates = []
[withoutDuplicates.append(x) for x in list if x not in withoutDuplicates]
print(withoutDuplicates)

# Task 5: Using list comprehension create a list that contains numbers from 10 to 1 in descending order.
list = [x for x in range (1, 11)]
list.reverse()
print(list)

# Task 6: Given a list [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]. You need to sort it in ascending order using any sorting algorithm. Do not user built-in "sort" or "sorted" method.
def bubble_sort(arr):

    a = len(arr)
    for i in range(a):
        for j in range (a - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

list = [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]
sorted_list = bubble_sort(list)
print(sorted_list)



# Tuples: 

# Task 1: Tuple Indexing
# Given a tuple my_tuple = (1, 2, 3, 4, 5), access and print the third element.

# Task 2: Tuple Slicing
# Given a tuple my_tuple = (1, 2, 3, 4, 5), create a new tuple that contains only the elements from index 2 to index 4 (inclusive).

# Task 3: Tuple Concatenation
# Given two tuples tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6), create a new tuple that is the concatenation of both tuples.

# Task 4: Tuple Unpacking
# Given the tuple my_tuple = ("John", 25, "USA"), unpack the elements into three separate variables named name, age, and country. Then, print the values of these variables.

# Task 5: Tuple Membership
# Given a tuple my_tuple = (1, 2, 3, 4, 5), check if the value 3 is present in the tuple. Print True if it is, and False otherwise.

# Task 6: Tuple Length
# Given a tuple my_tuple = ("apple", "banana", "cherry", "durian"), print the number of elements in the tuple.

# Task 7: Tuple Reversal
# Given a tuple my_tuple = (1, 2, 3, 4, 5), create a new tuple that contains the elements in reverse order.

# Task 8: Tuple Packing
# Create a tuple named person that contains the following information: the name "Alice", the age 28, and the country "Canada". Print the tuple.

# Task 9: Tuple Immutability
# Explain the concept of immutability in Python tuples and provide an example that demonstrates the immutability of tuples.

# Task 10: Tuple Conversion
# Given a list my_list = [1, 2, 3, 4, 5], convert it into a tuple named my_tuple. Print the resulting tuple.