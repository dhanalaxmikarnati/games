MAX_BOOKS = 3
library=["maths","sceinse","social","english","telugu","hindi"]
print("In Library available books are....")
for i in library:
    print(i)

class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    
class Book(Person):
    def __init__(self, name, age, phone_number,bookname, bookauthor):
        super().__init__(name, age, phone_number)
        self.bookname = bookname
        self.bookauthor = bookauthor

    def display_info(self):
        print(f"BookName: {self.bookname}, BookAuthor: {self.bookauthor}")

    def taken(self):
        print(f"{self.name} is taken book name  {self.bookname} of author {self.bookauthor} from library .")

class Library:
    def book():
        while True:
            global bks
            bks = input("Enter max no of books u want..on(1-"+str(MAX_BOOKS)+ ")?")
            if bks.isdigit():
               bks = int(bks)
               if 1<=bks<=MAX_BOOKS:
                    break
               else:
                    print("Enter valid number...")
            else:
                print("please enter a number between 1to 3..")  
        return bks
    
    def book_check():
       while True:
            bk=[(input("enter booknames..."))for bk in range(bks)]
            if bk in library:
                pass
            if len(bk)==bks:
                break
            else: 
                print("please enter existed bookname....")
       return bk
    def mem():
        mems=["dhana","avish","aadhya","varun","vihan","sitara"]
        m = (input("Enter existed librarian name?...."))
        while True:
            if m in mems:
               break
            else:
               m = (input("Enter existed name?...."))
        return m
    def pay():
        while True:
            amount = (input("Enter book cost? in Rupees...."))
            if amount.isdigit():
                amount = int(amount)
                if amount>0:
                    break
                else:
                    print("Enter valid amount...")
            else:
                print("please enter price of book..")  
        return amount
    
    bk=book()
    cb=book_check()
    me = mem()
    p=pay()
    print("\nlibrary Information:")
    print(f"LibrarianName:{me}")
    print(f"Bookname:{bk}") 
    print(f"Payment: {p}")
    print(f"BookList:{cb}")
    

if __name__ == "__main__":
    candidate_name = input("Enter candidate name....")
    candidate_age = int(input("Enter candidate age...."))
    candidate_phonenumber = int(input("Enter candidate phone number...."))
    book_name = input("Enter book name....")
    
    book_author = input("Enter book author name....")
    book = Book(candidate_name, candidate_age, candidate_phonenumber,book_name,book_author)
    l= Library()

    book.display_info()
    print()
    book.taken()
    print()
    

