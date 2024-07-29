class LibraryManager:
    def __init__(self):
        self.library = {}
    
    def add_book(self, title, author, publisher, volume, year, isbn):
        """Add a book to the library."""
        if isbn in self.library:
            print("Book with this ISBN already exists.")
        else:
            self.library[isbn] = {
                'Title': title,
                'Author': author,
                'Publisher': publisher,
                'Volume': volume,
                'Year': year,
                'ISBN': isbn
            }
            print("Book added successfully.")
    
    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.library:
            del self.library[isbn]
            print("Book removed successfully.")
        else:
            print("Book with this ISBN not found.")
    
    def retrieve_book(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        book = self.library.get(isbn)
        if book:
            return book
        else:
            print("Book with this ISBN not found.")
            return None
    
    def search_books(self, title=None, author=None):
        """Search for books by title or author."""
        results = []
        for book in self.library.values():
            if (title and title.lower() in book['Title'].lower()) or \
               (author and author.lower() in book['Author'].lower()):
                results.append(book)
        return results
    
    def list_books(self):
        """List all books currently in the library."""
        return list(self.library.values())
    
    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        """Update the details of an existing book."""
        if isbn in self.library:
            if title:
                self.library[isbn]['Title'] = title
            if author:
                self.library[isbn]['Author'] = author
            if publisher:
                self.library[isbn]['Publisher'] = publisher
            if volume:
                self.library[isbn]['Volume'] = volume
            if year:
                self.library[isbn]['Year'] = year
            print("Book details updated successfully.")
        else:
            print("Book with this ISBN not found.")
    
    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.library



from LibraryManager import LibraryManager


library = LibraryManager()


library.add_book('Introduction to Operating Systems', 'John Doe', 'Tech Publisher', '1', 2022, '978-1234567890')
library.add_book('Data Structures in Python', 'Jane Smith', 'Data Publisher', '2', 2021, '978-0987654321')
library.add_book('Machine Learning Basics', 'Alice Johnson', 'AI Publisher', '1', 2023, '978-1112131415')


library.remove_book('978-0987654321')


book = library.retrieve_book('978-1234567890')
print("Book Details:", book)


search_results = library.search_books(title='Machine Learning Basics')
print("Search Results by Title:", search_results)


search_results = library.search_books(author='John Doe')
print("Search Results by Author:", search_results)


all_books = library.list_books()
print("All Books:", all_books)


library.update_book('978-1234567890', title='Advanced Operating Systems')

is_available = library.check_availability('978-1234567890')
print("Book Availability:", is_available)
