import re


class LessonOne:
    # Given a string - “Hello, this is just a simple string for testing”. 
    # Make this string lower-cased, reverse all the separate words and take the last word out of it. 
    # Assign this word to a variable.
    string = 'Hello, this is just a simple string for testing'
    string_lowercase = string.lower()
    string_split = string_lowercase.split()
    reversed_string = [re.sub(r'\W', '', word[::-1]) for word in string_split]
    last_word = reversed_string[-1]
    print(last_word)

    #Given a url:‘https://localhost:8080/query?username=Dmytro&phone=1234567890
    # Using string methods extract from this url username and phone number and assign them to the separate variables ‘username’ and ‘phone’ accordingly

    url = 'https://localhost:8080/query?username=Dmytro&phone=1234567890'
    username_start_index = url.find("username=") + len("username=")
    username_end_index = url.find("&")
    username = url[username_start_index:username_end_index]
    phone_start_index=url.find("phone=") + len("phone=")
    phone = url[phone_start_index:]
    print(username)
    print(phone)
