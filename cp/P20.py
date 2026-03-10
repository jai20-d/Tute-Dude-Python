#write a python program to create a class book to create attribue and methods
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.publication_year}")
    def availability(self):
        print("Available in library")
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
book2 = Book("Dune", "Frank Herbert", 1965)
print("Book 1:")
book1.display_details()
print("Book 2:")
book2.display_details()
print("Availability for book 1:")
book1.availability()
print("Name : Jai Tomar")
print("Roll no: 2025UEA6527")