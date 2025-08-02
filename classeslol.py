class Books:
    # Constructor method
    def __init__(self, name, author, genre, price):
        self.name = name
        self.author = author
        self.genre = genre
        self.price = price

    # Method to display book details
    def display_details(self):
        print(f"I got a book called {self.name}. It was made by {self.author}. It is a {self.genre} book. It costs ${self.price}.")

# Creating an instance of Books
books = Books("I Was a Third Grade Spy", "Mary Jane Auch", "fiction", 7.99)

# Calling the method
books.display_details()

