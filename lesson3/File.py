# Task 1: File Reading
# Write a Python program that reads the contents of a text file named "hw_data.txt" and prints them to the console.

with open('lesson3\hw_data.txt') as file:
    print(file.read())

# Task 2: File Writing
# Write a Python program that prompts the user to enter some text and saves it to a text file named "output.txt".

someText = input("Type some text: ")
with open('lesson3\output.txt', 'w') as file:
    file.write(someText)

# Task 3: File Appending
# Write a Python program that prompts the user to enter a line of text and appends it to an existing text file named "hw_data.txt".

someText = input("Type some text: ")
with open('lesson3\hw_data.txt', 'a') as writer:
    writer.write('\n' + someText)

# Task 4: File Copying
# Write a Python program that reads the contents of a source file named "source.txt" and copies them to a destination file named "destination.txt".

with open("lesson3\source.txt", "r") as source, open("lesson3\destination.txt", "w") as destination:
    destination.write(source.read())

# Task 5: File Line Count
# Write a Python program that reads a text file named "hw_data.txt" and counts the number of lines in the file. Print the line count.

with open('lesson3\hw_data.txt') as file:
    print(len(file.readlines()))

# Task 6: File Word Count
# Write a Python program that reads a text file named "hw_data.txt" and counts the number of words in the file. Print the word count.

with open('lesson3\hw_data.txt') as file:
    data = file.read()
    print(len(data.split()))

# Task 7: File Searching
# Write a Python program that prompts the user to enter a search term and searches for occurrences of that term in a text file named "hw_data.txt". Print the line numbers where the search term is found.

searchTerm = input('Type text to search: ')
with open('lesson3\hw_data.txt') as file:
    fileLines = file.readlines()
for line in fileLines:
    if (searchTerm in line):
        print('Search term was found in line number: ', fileLines.index(line) + 1)

# Task 8: File Line Reversal
# Write a Python program that reads the contents of a text file named "hw_data.txt" and writes the lines in reverse order to a new text file named "reversed.txt".

with open('lesson3\hw_data.txt') as data, open('lesson3\data_reversed.txt', 'w') as reversed_data:
    reversed_data.writelines(reversed(data.readlines()))