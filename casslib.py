class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lundDict={}
        
def displayedBooks(self):
    print(f'We have the followiing books in our library: (self.name)')
    for book in self.booklist:
        print(book)
        
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated.You can take the book now")
            
        else:
            print(f"Book is already beig used by{self.lendDict[book]}")
            
    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")
        
    def returnbook(self,book):
        self.lendDict.pop(book)
        
if __name__=='__main__':
    
    books=Library(['Python','Rich Dad Poor Dad','Harry Porter,C++ Basics','Algorithms by CLRS'],"Lets Upskill")
    
    while(True):
        print(f"welcome to the {books.name} Library.Enter your choice to continue")
        print("1.Display books")
        print("2.lend a  book")
        print("3.add a  book")
        print("4.Return a book ")
        user_choice=input()
        if user_choice not in['1','2','3','4']:
            print("Please enter a valid option")
            continue
        
        else:
            user_choice=int(user_choice)
            
        if user_choice ==1:
            books.displayBooks()
            
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend")
            user=input("Enter your name")
            books.lendBook(user,book)
            
        elif user_choice==3:
            book=input("Enter the name of the book you want to add")
            books.addBook(book)
            
        elif user_choice==4:
            book=input("Enter the name of the book you want to return")
            books.returnbook(book)
            
        else:
            print("Not a vlid option")
            
        print("Press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="c"and user_choice2!="q"):
            user_choice2=input()
            if user_choice2 =="q":
                exit()
            
            elif user_choice2 =="c":
                continue
            
       
        
            
            
            
        