

class Book:
    def __init__(self,name,author,pages,ISBN):
        self.name=name
        self.author=author        
        self.pages=pages
        self.ISBN=ISBN

    def book_info(self):    
        print(f"Name: \"{self.name}\" Author: {self.author} Pages: {self.pages}")
        print(f"{self.ISBN}")

    def __str__(self) -> str:   
        print(f"Name: \"{self.name}\" Author: {self.author} Pages: {self.pages}")
        print(f"ISBN: {self.ISBN}")

g_ourell_1984=Book("1984","George Ourell",334,"978-0451524935")
g_ourell_1984.book_info()
    

        

