import mysql.connector
import pandas as pd

list_book = []
selected_book = []
cari = {}
func = {}
loader = {}

#untuk koneksi dengan database harus menyesuaikan dengan databas pada device maisng-masing
"""
DEVICE_AGUNG ADIPURWA dengan XAMPP
myDb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="22032002",
    database="book_shop"
)
"""
#DEVICE_SATYA
myDb=mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="2406",
    database="book_shop"
)

class Node:
    def __init__(self, book_id, title, author_name,
                 released_year, stock_quantity, price):
        self.left = None
        self.right = None
        self.book_id = book_id
        self.title = title
        self.author_name = author_name
        self.released_year = released_year
        self.stock_quantity = stock_quantity
        self.price = price

    def insert(self, book_id, title, author_name,
               released_year, stock_quantity, price):

        if released_year:
            if released_year <= self.released_year:
                if self.left is None:
                    self.left = Node(book_id, title, author_name,
                                     released_year, stock_quantity, price)
                else:
                    self.left.insert(book_id, title, author_name,
                                     released_year, stock_quantity, price)

            elif released_year > self.released_year:
                if self.right is None:
                    self.right = Node(book_id, title, author_name,
                                      released_year, stock_quantity, price)
                else:
                    self.right.insert(book_id, title, author_name,
                                      released_year, stock_quantity, price)
        else:
         self.book_id = book_id

    def traversePreOrder(self):
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def searching(self):
        atriDic = {1: self.book_id, 2: self.title, 3: self.author_name, 4: self.released_year,
                   5: self.stock_quantity, 6: self.price}
        count = 0
        if self:

            for key in cari.keys():
                if type(atriDic.get(key)) == str:
                    if atriDic.get(key).lower().find(cari.get(key).lower()) != -1:
                        count += 1
                elif atriDic.get(key) <= cari.get(key) and key == 6:
                    count += 1
                elif atriDic.get(key) == cari.get(key):
                    count += 1

            #print(count)

            if count == len(cari):
                #print("\n", self.book_id, self.title, self.author_name,
                #self.released_year, self.stock_quantity, self.price)
                loader = (self.book_id, self.title, self.author_name,
                          self.released_year, self.stock_quantity, self.price)
                selected_book.append(loader)
                #print(selected_book)

            #print(key_list, count)

            if self.right:
                self.right.searching()
            if self.left:
                self.left.searching()


def tableToList():
    kursor = myDb.cursor()
    kursor.execute("SELECT*FROM books")

    for row in kursor:
        list_book.append(row)


def listToBinaryTree():
    root = Node(list_book[0][0], list_book[0][1], list_book[0][2], list_book[0][3],
                list_book[0][4], list_book[0][5])

    for i in range(1, len(list_book)):
        root.insert(list_book[i][0], list_book[i][1], list_book[i][2], list_book[i][3],
                    list_book[i][4], list_book[i][5])

    return root


def select(choice_st,search_st):
    tableToList()
    root = listToBinaryTree()
    if choice_st == "Book Id":
        cari.update({1: int(search_st)})
        root.searching()
        df = pd.DataFrame(selected_book, columns=[
                'Book ID', 'Title', 'Author', 'Released Year', 'Stock', 'Price'])
        df = df.drop_duplicates(keep='first')

    elif choice_st == "Title":
        cari.update({2: str(search_st)})
        root.searching()
        df = pd.DataFrame(selected_book, columns=[
                'Book ID', 'Title', 'Author', 'Released Year', 'Stock', 'Price'])
        df = df.drop_duplicates(keep = 'first')

    elif choice_st == "Author":
        cari.update({3: str(search_st)})
        root.searching()
        df = pd.DataFrame(selected_book, columns=[
                'Book ID', 'Title', 'Author', 'Released Year', 'Stock', 'Price'])
        df = df.drop_duplicates(keep='first')
        
    for i in range(len(selected_book)):
       del selected_book[0]
    
    return df
