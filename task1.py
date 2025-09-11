library = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "Hamlet", "author": "William Shakespeare", "year": 1603},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997},
]

borrow=[]

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))

    library.append({"title": title, "author": author, "year": year})
    print('Book was added')

def find_book():
    title=input("Enter book title: ")

    found=False
    for books in library:
        if books['title']==title:
            print(books)
            found=True
    if not found:
        print('Book not found')
    print()

def show_books():
    for i, books in enumerate(library,1):
        print(f"{i}. {books['title']}    {books['author']}   {books['year']}")
    print()
    
        
    
def borrow_book():
    show_books()
    book_num=int(input('Enter book number : '))
    if book_num in range(1,len(library)+1):
        book=library.pop(book_num-1)
        borrow.append(book)
        print('Done.')
    else:
        print('Wrong number')


def main():
    while True:
        print('Choices : ')
        print("1. Show all books")
        print("2. Add a book")
        print("3. Find a book (by title) ")
        print("4. Borrow a book")
        print("5. Exit")
        print()


        choice=int(input('Your choice : '))

        match choice:
            case 1:
                show_books()
            case 2:
                add_book()
            case 3:
                find_book()
            case 4:
                borrow_book()
            case 5:
                break

main()