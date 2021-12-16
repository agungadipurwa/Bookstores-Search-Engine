import mysql.connector
import pandas as pd


list_book = []
selected_book = []
func = {}
loader = {}

#This database isn't you can custom based on what you have. So, you must use our database especialy the format of table.
#DEVICE AGUNG ADIPURWA with XAMPP and phpmyadmin
#This database isn't you can custom based on what you have.
myDb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="22032002",
    database="gramedia"
)

#DEVICE SATYA
"""
myDb=mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="2406",
    database="book_shop"
)
"""

#DEVICE DIRGA
"""
myDb=mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="2406",
    database="book_shop"
)
"""

class Node:
    def __init__(self, book_id, title, author_name,
                 released_year, location, stock_quantity, price):
        self.left = None
        self.right = None
        self.book_id = book_id
        self.title = title
        self.author_name = author_name
        self.released_year = released_year
        self.location = location
        self.stock_quantity = stock_quantity
        self.price = price

    def insert(self, book_id, title, author_name,
               released_year, location, stock_quantity, price):

        if released_year:
            if released_year <= self.released_year:
                if self.left is None:
                    self.left = Node(book_id, title, author_name,
                                     released_year, location, stock_quantity, price)
                else:
                    self.left.insert(book_id, title, author_name,
                                     released_year, location, stock_quantity, price)

            elif released_year > self.released_year:
                if self.right is None:
                    self.right = Node(book_id, title, author_name,
                                      released_year, location, stock_quantity, price)
                else:
                    self.right.insert(book_id, title, author_name,
                                      released_year, location, stock_quantity, price)
        else:
         self.book_id = book_id

    def traversePreOrder(self):
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def searching(self, cari):
        atriDic = {1: self.book_id, 2: self.title, 3: self.author_name, 4: self.released_year, 5: self.location,
                   6: self.stock_quantity, 7: self.price}
        count = 0
        if self:

            for key in cari.keys():
                if type(atriDic.get(key)) == str:
                    if atriDic.get(key).lower().find(cari.get(key).lower()) != -1:
                        count += 1
                elif atriDic.get(key) <= cari.get(key) and key == 7:
                    count += 1
                elif atriDic.get(key) == cari.get(key):
                    count += 1

            if count == len(cari):
                loader = (self.book_id, self.title, self.author_name,
                          self.released_year, self.location, self.stock_quantity, self.price)
                selected_book.append(loader)

            if self.right:
                self.right.searching(cari)
            if self.left:
                self.left.searching(cari)


def tableToList():
    kursor = myDb.cursor()
    kursor.execute("SELECT*FROM books_db")
    for row in kursor:
        list_book.append(row)

def listToBinaryTree():
    root = Node(list_book[0][0], list_book[0][1], list_book[0][2], list_book[0][3],
                list_book[0][4], list_book[0][5], list_book[0][6])

    for i in range(1, len(list_book)):
        root.insert(list_book[i][0], list_book[i][1], list_book[i][2], list_book[i][3],
                    list_book[i][4], list_book[i][5], list_book[i][6])

    return root

def select(choice_st,search_st):
    tableToList()
    root = listToBinaryTree()
    cari = {}
    if choice_st == "Book ID":
        cari.update({1: int(search_st)})
        root.searching(cari)
        df = pd.DataFrame(selected_book, columns=[
                'Book ID', 'Title', 'Author', 'Released Year', 'Location', 'Stock', 'Price'])
        df = df.drop_duplicates(keep='first')

    elif choice_st == "Title":
        cari.update({2: str(search_st)})
        root.searching(cari)
        df = pd.DataFrame(selected_book, columns=[
                'Book ID', 'Title', 'Author', 'Released Year','Location', 'Stock', 'Price'])
        df = df.drop_duplicates(keep = 'first')

    elif choice_st == "Author" :
        cari.update({3: str(search_st)})
        root.searching(cari)
        df = pd.DataFrame(selected_book, columns=[
                'Book ID', 'Title', 'Author', 'Released Year','Location', 'Stock', 'Price'])
        df = df.drop_duplicates(keep='first')
    

    for i in range(len(selected_book)):
       del selected_book[0]

    cari = {}
    return df
