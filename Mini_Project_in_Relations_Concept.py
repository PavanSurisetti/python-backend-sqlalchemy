# Create:
# Author → Books
# Insert:
# 1 author with 3 books
# Fetch:
# Print all books of that author
# Reverse:
# Print author of a book
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
Base=declarative_base()#this is used to recognize the class as table
class author(Base):
    __tablename__='AuthorTable'
    aid=Column(Integer,primary_key=True)#this is the author id that is  used to recognize the author uniquely
    aname=Column(String)#this is the author name 
    book_relation=relationship('book',back_populates='author_relation')
class book(Base):
    __tablename__='BooksTable'
    bid=Column(Integer,primary_key=True)# this is the book id that is used to unqiuely identify each book
    bname=Column(String)#this is the book name
    aid=Column(Integer,ForeignKey('AuthorTable.aid'))
    author_relation=relationship('author',back_populates='book_relation')
engine=create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
a1=author(aid=1,aname='Ganesha')
a2=author(aid=2,aname='Satya')
a3=author(aid=3,aname='Pavan')
a4=author(aid=4,aname='Pavan Satya')
a5=author(aid=5,aname='Ram')
session.add_all([a1,a2,a3,a4,a5])#added here
session.commit()#succesfully saved into database
b1=book(bid=1001,bname='Python',aid=1)
b2=book(bid=1002,bname='Data Science using Python',aid=1)
b3=book(bid=1003,bname='DSA',aid=1)
b4=book(bid=1004,bname='C',aid=2)
b5=book(bid=1005,bname='C#',aid=2)
b6=book(bid=1006,bname='C++',aid=2)
b7=book(bid=1007,bname='Numpy',aid=3)
b8=book(bid=1008,bname='Matplotlib',aid=3)
b9=book(bid=1009,bname='FastAPI',aid=4)
b10=book(bid=1010,bname='SQL',aid=5)
session.add_all([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10])
session.commit()#data added to DB successfully
#let's print the data from Author Table
AT=session.query(author).all()#author Table contents fetching from the database
print('Author Table \n aid \t aname')
for i in AT:
    print(i.aid,i.aname)
BT=session.query(book).all()#book table contents fetching from the database
print('Book Table \n bid \t bname\t aid')
for i in BT:
    print(i.bid,i.bname,i.aid)
#let's fetch the author table data using the book table
temp1=session.query(book).all()
print(' fetching the author details using book table')
for i in temp1:#1-1 relationship
    print(f'Author ID:{i.aid},Author Name:{i.author_relation.aname},Book Name:{i.bname}')
#lets fetch the book table data using the author table
print('fetching the book table data using the author table')
temp2=session.query(author).all()
for i in temp2:#this is 1-M relationship
    for j in i.book_relation:# we fetch the same author for mutliple books
        print(f'Author ID:{i.aid},Author Name:{i.aname},Book iD:{j.bid}, Book Name:{j.bname}')
