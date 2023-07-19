# Rewrite the following class to use getters and setters to access object fields.

class Contact:

    def __init__(self, first_name, last_name, phone_number, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, value):
        self.first_name = value

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, value):
        self.last_name = value

    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, value):
        self.phone_number = value

    def get_email(self):
        return self.email
    
    def set_email(self, value):
        self.email = value
