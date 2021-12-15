import mysql.connector
import pandas as pd

list_book = []
selected_book = []
func = {}
loader = {}

#This database isn't you can custom based on what you have.
#DEVICE_AGUNG ADIPURWA dengan XAMPP
myDb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="22032002",
    database="book_shop"
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
        released_year, stock_quantity, price):
        self.left=None
        self.right=None
        self.book_id=book_id
        self.title=title
        self.author_name=author_name 
        self.released_year=released_year
        self.stock_quantity=stock_quantity
        self.price=price
    
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
        print(self.book_id, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def searching(self, cari):
        atriDic={1:self.book_id, 2:self.title, 3:self.author_name, 4:self.released_year,
        5:self.stock_quantity, 6:self.price}
        count=0
        if self:
    
           
            for key in cari.keys():
                if type(atriDic.get(key))==str:
                    if atriDic.get(key).lower().find(cari.get(key).lower())!=-1:
                        count+=1
                elif atriDic.get(key)<=cari.get(key) and key==6:
                    count+=1
                elif atriDic.get(key)==cari.get(key):
                    count+=1
           
                
            
            #print(count)
            
            if count==len(cari):
                #print("\n", self.book_id, self.title, self.author_name,
                #self.released_year, self.stock_quantity, self.price)
                loader=(self.book_id, self.title, self.author_name,
                self.released_year, self.stock_quantity, self.price)
                selected_book.append(loader)
                #print(selected_book)
            
            #print(key_list, count)
            
          

            if self.right:
                self.right.searching(cari)
            if self.left:
                self.left.searching(cari)      
         
        

   
def tableToList():
    kursor=myDb.cursor()
    kursor.execute("SELECT*FROM books")
    
    
    for row in kursor:
        list_book.append(row)
        #print(row)
    print(list_book)

def listToBinaryTree():
    root=Node(list_book[0][0], list_book[0][1], list_book[0][2], list_book[0][3],
                list_book[0][4], list_book[0][5])

    for i in range(1, len(list_book)):
        root.insert(list_book[i][0], list_book[i][1], list_book[i][2], list_book[i][3],
        list_book[i][4], list_book[i][5])
    
    return root

def main():
    tableToList()
    root=listToBinaryTree()
    cari={}
    while True:
        
        print("Cari buku melalui apa: ")
        print("1. Kode Buku\n2. Judul Buku\n3. Nama Penulis")
        print("4. Tahun Terbit\n5. Jumlah Buku\n6. Maksimal Harga\n7. cari")
        x=int(input("Masukan nomer pilian: "))
        
        if x==1:
            cari.update({1:int(input("Kode Buku: "))})
        elif x==2:
            cari.update({2:str(input("Judul buku: "))})
        elif x==3:
            cari.update({3:str(input("Nama penulis: "))})
        elif x==4:
            cari.update({4:int(input("Tahun terbit: "))})
        elif x==5:
            cari.update({5:int(input("Jumlah buku: "))})
        elif x==6:
            cari.update({6:int(input("Maksimal harga: "))})
        elif x==7:
            print(cari)
            root.searching(cari)
            print(selected_book)
            for i in range(len(selected_book)):
                del selected_book[0]
            cari={}
        

    #printing(root)

    #print("Pre order Traversal: ", end="")
    #root.traversePreOrder()
    


if __name__=="__main__":
    main()
