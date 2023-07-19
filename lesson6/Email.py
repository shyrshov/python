# Task 5: Email

# Create a Python class called "Email" with the following properties and methods:

# Properties:

# sender (string)
# recipient (string)
# subject (string)
# body (string)
# Methods:

# send(): Prints the email's sender, recipient, subject, and body in the following format:
# "From: [sender]
# To: [recipient]
# Subject: [subject]
# Body: [body]"
# Feel free to modify or extend these tasks based on your requirements.

class Email:

    def __init__(self, sender: str, recipient: str, subjet: str, body: str):
        self.sender = sender
        self.recipient = recipient
        self.subject = subjet
        self.body = body
    
    def send(self):
        print("From: [%s]\nTo: [%s]\nSubject: [%s]\nBody: [%s]" % (self.sender, self.recipient, self.subject, self.body))

email= Email("andrii.shyrshov@customertimes.com", "helpdesk@customertimes.com", "Need help", "I need help with VPN. Please call me")
email.send()