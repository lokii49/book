class Book:
    def __init__(self, pages, price, author, id, title):
        self.pages = pages
        self.price = price
        self.author = author
        self.id = id
        self.title = title

class BookStore:
    def __init__(self, bookStoreName, BookList):
        self.bookStoreName = bookStoreName
        self.BookList = BookList

    def findMinimumBookByid(self):
        ids = []
        details = []
        for item in self.BookList:
            ids.append(item.id)
        mini = min(ids)
        for item in self.BookList:
            if mini == item.id:
                details.append(item.pages)
                details.append(item.price)
                details.append(item.author)
                details.append(item.id)
                details.append(item.title)
        if ids == 0:
            return None
        else:
            return details

    def sortBookByid(self):
        ids = []
        for item in self.BookList:
            ids.append(item.id)
        idSort = sorted(ids)
        return idSort


if __name__ == '__main__':
    num = int(input())
    BookList = []
    for i in range(num):
        pages = int(input())
        price = int(input())
        author = input()
        id = int(input())
        title = input()
        BookList.append(Book(pages, price, author, id, title))
    bookStoreName = None
    obj = BookStore(bookStoreName, BookList)
    result1 = obj.findMinimumBookByid()
    for i in result1:
        print(i)
    result2 = obj.sortBookByid()
    for i in result2:
        print(i)
