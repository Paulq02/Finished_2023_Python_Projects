class Book:

    def __init__(self,title,author,genre) -> None:
        self.title=title
        self.author=author
        self.genre=genre

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    

book_1=Book("lion king","elton john","fantasy")
print(book_1.get_author())
        