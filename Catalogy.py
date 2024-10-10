
available_books = []
new_books_queue = []
undo_stack = []
def add_new_book(book):
    new_books_queue.append(book)
    print(f"New book '{book}' added to the new books queue.")

def process_next_book():
    if len(new_books_queue) > 0:
        book = new_books_queue.pop(0)
        available_books.append(book)
        undo_stack.append(("add", book))  
        print(f"Book '{book}' processed and added to available books.")
    else:
        print("No new books to process.")

def undo_last_update():
    if len(undo_stack) > 0:
        action, book = undo_stack.pop()  
        if action == "add" and book in available_books:
            available_books.remove(book)
            print(f"Undo: Book '{book}' removed from available books.")
    else:
        print("No actions to undo.")

def display_catalog():
    print("\nLibrary Catalog")
    print("Available books:", available_books)
    print("New books in queue:", new_books_queue)
    print("Undo stack:", undo_stack)
  

def library_management(action, book=None):
    if action == "add_new_book" and book:
        add_new_book(book)
    elif action == "process_next_book":
        process_next_book()
    elif action == "undo_last_update":
        undo_last_update()
    elif action == "display_catalog":
        display_catalog()
    else:
        print("Invalid action or missing book title.")


library_management("add_new_book", "The Great Gatsby")
library_management("add_new_book", "1984")
library_management("add_new_book", "To Kill a Mockingbird")

library_management("display_catalog") 

library_management("process_next_book") 
library_management("process_next_book")

library_management("display_catalog") 

library_management("undo_last_update")  

library_management("display_catalog") 