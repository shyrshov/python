class Contact:

    def __init__(self, first_name, last_name, phone_number, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    @property
    def first_name(self):
        print("Property method 'first_name' was called.")
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        print("Property method 'last_name' was called")
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def phone_number(self):
        print("Property method 'phone_number' was called")
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def email(self):
        print("Property method 'email' was called")
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value