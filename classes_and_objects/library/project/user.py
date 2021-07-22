from library import Library

class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            library.rented_books[self.username] = {book_name:days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        elif book_name in library.rented_books.values():
            for user in library.rented_books.keys():
                if book_name in library.rented_books[user]:
                    return f"The book \"{book_name}\" is already rented and will be available in {library.rented_books[user][book_name]} days!"

    def return_book(self, author:str, book_name:str, library: Library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return "info function"
        
    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"



