# 1) Write a function called calculate_rectangle_area that calculates and returns the area of a rectangle. 
# The function should take two positional arguments: length and width.

def calculate_rectangle_area(length, wigth):
    return length*wigth
print(calculate_rectangle_area(4,5))

# 2) Create a function called print_student_details that prints the details of a student. 
# The function should take three keyword arguments: name, age, and grade.

def print_student_details(name, age, grade):
    print('Name: ', name)
    print('Age:', age)
    print('Grade:', grade)
print_student_details('Ann', 20, 'second')

# 3) Implement a function called calculate_expenses that calculates and returns the total expenses for a trip. 
# The function should take one positional argument hotel_cost, and two keyword arguments: food_cost and transportation_cost.
#  Assume that food_cost and transportation_cost have default values of 0.

def calculate_expenses(hotel_cost, food_cost=0, transportation_cost=0):
    return ('Total expenses: {}'.format(hotel_cost + food_cost + transportation_cost))
print(calculate_expenses(1000, 100))

# 4) Write a function called send_email that sends an email to a recipient(console output). 
# The function should take a positional argument recipient and two keyword arguments: subject and body. 
# The subject argument should have a default value of "Important Message" and the body argument should have 
# a default value of an empty string.

def send_email(recipient, subject='Important Message', body=''):
    print('Recipient: ', recipient)
    print('Subject: ', subject)
    print('Body:', body)
send_email('andrii.shyrshov@customertimes.com', body='This is a test message')

# 5) Create a function called print_song_details that prints the details of a song. 
# The function should take two positional arguments: title and artist, and three keyword arguments: duration, genre, and year. 
# Assume that duration has a default value of 0, genre has a default value of "Unknown", and year has a default value of None.

def print_song_details(title, artist, duration=0, genre='Unknown', year=None):
    print('Song details are: Title: [{}], Artist: [{}], Duration: [{}], Genre: [{}], Year: [{}]'.format(title, artist, duration, genre, year))
print_song_details('New song', 'Somebody', year=2023)

# 6) Implement a function called calculate_shipping_cost that calculates and returns the shipping cost for an item. 
# The function should take two positional arguments: item_price and weight, and one keyword argument discount. 
# Assume that discount has a default value of 0.

def calculate_shipping_cost(item_price, weight, discount=0):
    if discount > 100 or discount < 0:
        return 'Discount value should be between 0 and 100'
    else: 
        return 'Shipping cost is: ', item_price * weight * (1 - discount/100)
print(calculate_shipping_cost(1, 1, 99))

# 7) Write a function called print_book_details that prints the details of a book. 
# The function should take a positional argument title and two keyword arguments: author and publication_year. 
# Assume that publication_year has a default value of None.

def print_book_details(title, author, publication_year=None):
    print('Book title is: ', title)
    print('Author is: ', author)
    print('Publication year is: ', publication_year)
print_book_details('Inetersting book', 'New Author')

# 8) Create a function called calculate_total_cost that calculates and returns the total cost of a purchase.
#  The function should take one positional argument base_price and two keyword arguments: tax_rate and discount. 
# Assume that tax_rate has a default value of 0 and discount has a default value of 0.

def calculate_total_cost(base_price, tax_rate=0, discount=0):
    if discount > 100 or discount < 0 or tax_rate < 0:
        return "Discount value should be between 0 and 100. Tax rate shouldn't be less than 0"
    else: 
        price_with_discount = base_price * (1 - discount/100)
        return 'Total cost is: ', price_with_discount + price_with_discount * (tax_rate/100)
print(calculate_total_cost(10, 10, 50))

# 9) Implement a function called convert_temperature that converts a temperature from Celsius to Fahrenheit. 
# The function should take a positional argument celsius and one keyword argument round_digits. 
# Assume that round_digits has a default value of 2.

def convert_temperature(celsius, round_digits = 2):
    return round(((1.8 * celsius) + 32), round_digits)
print(convert_temperature(38))

# 10) Write a function called print_invoice that prints an invoice for a purchase. 
# The function should take a positional argument customer_name and two keyword arguments: 
# items (a list of purchased items) and discount. Assume that discount has a default value of 0.

def print_invoice(customer_name, items, discount=0):
    print('Customer name: ', customer_name)
    for i in items:
        print('Product: {}, discount: {}'.format(i, discount))
print_invoice('Andrii', ['apple', 'lemon', 'juice'])

# 11) Create a function with one parameter as integer that returns True is if the given number is prime number or False otherwise.

def is_prime_number(number: int):
    if number == 1:
        return "It's not a prime number"
    elif number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
print(is_prime_number(2))

# 12) Create a function that returns fibonacci sequence with the given number of elements in a tuple. 
# For example: fib(5) should return (0, 1, 1, 2, 3).

def fib(number):
    sequence = []
    a = 0
    b = 1
    for i in range(number):
        sequence.append(a)
        next = a + b
        a = b
        b = next
    return tuple(sequence)
print(fib(5))
