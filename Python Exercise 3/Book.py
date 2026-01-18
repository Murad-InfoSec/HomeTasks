

# Book class
class Book:
    # Initialize book
    def __init__(self,name,author,pages,ISBN):
        self.name=name
        self.author=author        
        self.pages=pages
        self.ISBN=ISBN

    # Print book info
    def book_info(self):    
        print(f"Name: \"{self.name}\" Author: {self.author} Pages: {self.pages}")
        print(f"{self.ISBN}")

    # String representation
    def __str__(self) -> str:   
        print(f"Name: \"{self.name}\" Author: {self.author} Pages: {self.pages}")
        print(f"ISBN: {self.ISBN}")

# Create book instance
g_ourell_1984=Book("1984","George Ourell",334,"978-0451524935")
# Print info
g_ourell_1984.book_info()
    

        
