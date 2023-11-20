MAX_BOOKS = 3
library = ["maths", "science", "social", "english", "telugu", "hindi"]

print("In Library available books are....")
for i in library:
    print(i)


class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number


class Book(Person):
    def __init__(self, name, age, phone_number, bookname, bookauthor):
        super().__init__(name, age, phone_number)
        self.bookname = bookname
        self.bookauthor = bookauthor

    def display_info(self):
        print(f"BookName: {self.bookname}, BookAuthor: {self.bookauthor}")

    def taken(self):
        print(f"{self.name} has taken the book {self.bookname} by author {self.bookauthor} from the library.")


class Library:
    def book(self):
        while True:
            global bks
            bks = input("Enter the maximum number of books you want (1-" + str(MAX_BOOKS) + "): ")
            if bks.isdigit():
                bks = int(bks)
                if 1 <= bks <= MAX_BOOKS:
                    break
                else:
                    print("Enter a valid number...")
            else:
                print("Please enter a number between 1 to 3...")

        return bks

    def book_check(self):
        while True:
            bk = [input("Enter book names...") for _ in range(bks)]
            if all(item in library for item in bk):
                break
            else:
                print("Please enter existing book names....")

        return bk

    def mem(self):
        mems = ["dhana", "avish", "aadhya", "varun", "vihan", "sitara"]
        m = input("Enter the existing librarian name: ")
        while True:
            if m in mems:
                break
            else:
                m = input("Enter an existing name: ")

        return m

    def pay(self):
        while True:
            amount = input("Enter the book cost in Rupees: ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Enter a valid amount...")
            else:
                print("Please enter the price of the book...")

        return amount


if __name__ == "__main__":
    candidate_name = input("Enter candidate name: ")
    candidate_age = int(input("Enter candidate age: "))
    candidate_phonenumber = int(input("Enter candidate phone number: "))
    book_name = input("Enter book name: ")
    book_author = input("Enter book author name: ")

    book = Book(candidate_name, candidate_age, candidate_phonenumber, book_name, book_author)
    l = Library()

    book.display_info()
    print()
    book.taken()
    print()

    bk = l.book()
    cb = l.book_check()
    me = l.mem()
    p = l.pay()

    print("\nLibrary Information:")
    print(f"Librarian Name: {me}")
    print(f"Book Name: {bk}")
    print(f"Payment: {p}")
    print(f"Book List: {cb}")
