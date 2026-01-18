# Contact class to store and manage contact information


class Contact:
    # Constructor: initializes a Contact object with name and phone number
    def __init__(self,name,number):
        self.name=name
        self.number=number

    # Method to simulate calling a contact - prints calling information
    def call(self):
        print(f"You are calling \"{self.name}\"\t{self.number}")

    # String representation method - defines how Contact objects are displayed as strings
    def __str__(self) :
        print(f"You are calling \"{self.name}\"\t{self.number}")

# Create a Contact instance for Zaur Alixanov
z_alixanov=Contact("Zaur Alixanov","09965456323")
# Call the contact
z_alixanov.call()
