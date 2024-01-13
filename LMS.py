import mysql.connector
mydb= mysql.connector.connect(host='localhost',user='root',\
                             passwd='qwerty!@#$%^',database='library')

def addmb():
    n= int (input ("Enter the number of books you want to add: "))
    for i in range(n):
        bn=input ("Enter book name: ")
        c= input ("Enter book code: ")
        t= input("Total books: ")
        s=input("Enter subject: ")
        data= (bn,c,t,s)
        a= 'insert into books values(%s,%s,%s,%s)'
        c=mydb.cursor()
        c.execute(a,data)
        mydb.commit()
    print ("Data entered successfully!")
def issueb():
    n=input ("Enter member name: ")
    r= input("Enter registration number of the member: ")
    co= input ("Enter book code of the book issued to the member: ")
    d=input("Enter date: ")
    data= (n,r,co,d)
    query= 'insert into issue values(%s,%s,%s,%s)'
    c=mydb.cursor()
    c.execute(query,data)
    mydb.commit()
    print ("Book issued to",n)
    bookup(co,-1)
def submitb():
    n=input ("Enter member name: ")
    r= input("Enter registration number of the member: ")
    co= input ("Enter book code of the book submitted by the member: ")
    d=input("Enter date: ")
    data= (n,r,co,d)
    query= 'insert into submit values(%s,%s,%s,%s)'
    c=mydb.cursor()
    c.execute(query,data)
    mydb.commit()
    print ("Book submitted by",n)
    bookup(co,1)
def bookup(co,u):
    a= 'select totalbooks from books where bcode=%s'
    data=(co,)
    c= mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t= myresult[0]+u
    query="update books set totalbooks=%s where bcode=%s"
    d=(t,co)
    c.execute(query,d)
    mydb.commit()
def delb():
    ac= input ("Enter book code: ")
    a="delete from books where bcode=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(a,data)
    mydb.commit()
def searchb():
    ac= input ("Enter book code: ")
    a="select* from books where bcode=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(a,data)
    res=c.fetchall()
    for i in res:
        print("Book name: ",i[0])
        print("Book code: ",i[1])
        print("Total no of books: ",i[2])
        print ("Subject: ",i[3])
    
def displayb():
    a="select * from books"
    c=mydb.cursor()
    c.execute(a)
    myres=c.fetchall()
    for i in myres:
        print("Book name: ",i[0])
        print("Book code: ",i[1])
        print("Total no of books: ",i[2])
        print("Subject: ",i[3])
def main():
    print ('''
    1. ADD BOOKS
    2. ISSUE BOOK
    3. SUBMIT BOOK
    4. DELETE BOOK
    5. SEARCH BOOK BY CODE
    6. DISPLAY BOOKS
    ''')
    choice=input ("Enter your choice: ")
    if choice=="1":
        addmb()
    elif choice=="2":
        issueb()
    elif choice=="3":
        submitb()
    elif choice=="4":
        delb()
    elif choice=="5":
        searchb()
    elif choice=="6":
        displayb()
    else:
        print ("Wrong choice...")
def pwd():
    pw= input ("Enter password of LMS: ")
    if pw=="1234":
        main()
    else:
        print("Wrong password...")
        pwd()
def runAgain():
    runAgn = input("\n Do you want To Run Again Y/n: ")
    while (runAgn.lower() == 'y'):
        main()
        runAgn = input("\n Do you want To Run Again Y/n: ")
pwd()
runAgain()

