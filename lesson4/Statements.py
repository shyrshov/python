import random
# Task: Number Guessing Game
# Write a Python program that generates a random number between 1 and 100. Allow the user to guess the number, and provide appropriate
#  feedback (e.g., "Too high" or "Too low") until they guess the correct number. 
# Use a loop and conditional statements to implement the game.

randomInt = random.randint(1, 100)
tryToGuess = 'Try to guess the number in range from 1 to 100: '
print(randomInt)
userInt = int(input(tryToGuess))
print(userInt)
while userInt != randomInt:
    if userInt > randomInt:
        print('Too high')
        userInt = int(input(tryToGuess))
    elif userInt < randomInt:
        print('Too low')
        userInt = int(input(tryToGuess))
print('You won the game')

# Task: Character Counter
# Write a Python program that takes a string as input from the user and counts the number of occurrences of each character in the string. 
# Display the result in the format: "Character: Count". Use loops and conditional statements to implement this.

userString = input('Type a random string: ')
d = {}
for i in userString:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i]+1
print(d)

# Task: Password Strength Checker
# Write a Python program that takes a password as input from the user and checks its strength. Display a message indicating whether
#  the password is weak, moderate, or strong based on the following criteria:

# Weak: Less than 8 characters long
# Moderate: 8 to 12 characters long
# Strong: More than 12 characters long
# Use conditional statements to determine the strength.

p = input('Please, set your password: ')
if len(p) < 8:
    print('Password is weak')
elif len(p) <= 12:
    print('Password is moderate')
else:
    print('Password is strong')


# Task: Number Sum
# Write a Python program that takes an integer as input from the user and calculates the sum of all numbers from 1 to that integer 
# (inclusive). Display the result. Use a loop and conditional statements to implement this.

number = int(input('Type an integer: '))
i = 1
result = 0

for i in range(1, number + 1):
    result += i
print('Sum of all numbers from 1 to {} is {}'.format(number, result))


# Task: Palindrome Checker
# Write a Python program that takes a string as input from the user and checks whether it is a palindrome. A palindrome is a word, 
# phrase, number, or other sequence of characters that reads the same forward and backward. 
# Display a message indicating whether the string is a palindrome or not. Use loops and conditional statements to implement this.

string = input('Type anything: ')
isPalindtome = 'Palindrome'
for x in range(0, len(string)):
    if string[x] != string[::-1][x]:
        isPalindtome = 'Not palindrome'
        break  
print('Input string is: {}'.format(isPalindtome))

# Task: Multiplication Table
# Write a Python program that takes an integer as input from the user and prints the multiplication table for that number from 1 to 10. 
# Display the result in the format: "Number x Multiplier = Result". Use loops and conditional statements to implement this.

number = int(input('Type the number to multiply: '))
for i in range (1, 11):
    print('{} x {} = {}'.format(number, i, number*i))

# Task: Vowel Counter
# Write a Python program that takes a string as input from the user and counts the number of vowels (a, e, i, o, u)
#  in the string. Display the result. Use loops and conditional statements to implement this.

string = input('Type any string: ')
vowels = 0
for i in string:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels +=1
print('Number of vowels: ', vowels)
