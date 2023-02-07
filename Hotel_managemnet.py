"""
Author: Sourabh Shukla
Date: 07-02-2023

"""
import os
import platform
import mysql.connector as s
import datetime

class roombooking:
    def __init__(self):
        self.mydb=s.connect(host="localhost",user="testuser",password="testuser",database="testingdb")
        try:
            self.mydb=s.connect(**self.conn)
            print("Connected to Mysql")
            
        except:
            print("Not connected")
      
        self.custdata="create table if not exists custdata(custno varchar(15),custname varchar(20),addr varchar(200),in_date date,out_date date)"
        self.reciept="create table if not exists reciept(custno varchar(25),reciept_tot int(10))"
        
        #create the cursor
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute(self.custdata)
    
        #query execute
        self.mycursor.execute(self.reciept)
     
        #save the changes
        self.mydb.commit()
        
    def registercust(self):
        L=[]
        custno=int(input('Enter customer no='))
        L.append(custno)
        custname=input('Enter name:')
        L.append(custname)
        addr=input('Enter address:')
        L.append(addr)
        in_date=input('Enter checkin date:')
        L.append(in_date)
        # in_date=in_date.split("-")
        out_date=input('Enter checkout date:')
        L.append(out_date)  
        # out_date=out_date.split("-")
        cust=(L)
        sql='insert into custdata(custno,custname,addr,in_date,out_date) values(%s,%s,%s,%s,%s)'
        self.mycursor.execute(sql,cust)
        self.mydb.commit()
        in_date=in_date.split("-")
        out_date=out_date.split("-")

        C=[]
        C.append(custno)
        print("\nWe have the following rooms for you-\n1. type A--->rs 1000 PN\-,\n2. type B--->rs 2000 PN\-,\n3. type c--->rs 3000 PN\-,\n4. typr D--->rs 4000 PN\-")
        x=int(input('Enter your choice:'))
        # n=""
        # if in_date[1]==out_date[1]:
        n=int(out_date[2])-int(in_date[2])
        # else:
        #     np=int(out_date[2])-int(in_date[2]C
        if x==1:
            print('you have opted type A.')
            s=1000*n
            # C.append(s)
        elif x==2:
            print('you have opted type B.')
            s=2000*n
            # C.append(s)
        elif x==3:
            print('you have opted type c.')
            s=3000*n
            # C.append(s)
        elif x==4:
            print("you have opted type D.")
            s=4000*n
            # C.append(s)    
        else:
            print('Please choose a room.')
        print('your room rent  is =',s,'\n')
        print(' child charge 1000 rs per child')
        
        y=int(input('Enter your how many child :'))
        z=y*1000
        # C.append(z)
        reciept=(s+z)
        print('Your Totalbill:',s+z,'\n')
        reciept_tot=s+z
        C.append(reciept_tot)
        print("This is , ",C)
        reciept=(C)
        sql="insert into reciept (custno,reciept_tot) values (%s,%s)"
        self.mycursor.execute(sql,reciept)
        self.mydb.commit() 
    
 
    def sis(self):
        custno=int(input("Enter the customer number whose bill to be viewed : "))
        sql="Select custdata.custno, custdata.custname, custdata.addr,custdata.in_date,custdata.out_date,reciept.custno, reciept.reciept_tot from custdata INNER JOIN reciept ON custdata.custno=reciept.custno and reciept.custno = %s"
        rl=(custno,)
        self.mycursor.execute(sql,rl)
        res=self.mycursor.fetchall()
        for x in res:
            print(f"Hey {x[1]}, your total bill amount is {x[6]}")

    def dispall(self):
        sql="select custdata.custno, custdata.custname, custdata.addr,custdata.in_datedate,custdata.out_date,reciept._tot,reciept.child_tot,g_tot from custdata INNER JOIN reciept ON custdata.custno=reciept.custno" 
        self.mycursor.execute(sql)   
        res=self.mycursor.fetchall()
        print("The Customer details are as follows : ")
        
        for x in res:
            print(x)
        
Hotel_Stars= roombooking()

def Menuset():
    print('Enter 1: To enter customer data.')
    print('Enter 2: For billamount.')
    print('Enter 3: Display customerwise Details.')
    print('Enter 4: Display All Details.')
    print('Enter 5: Exit')
    
    userinput=int(input('Enter your choice:'))
    if userinput==1:
        Hotel_Stars.registercust()
    elif userinput==2:
        Hotel_Stars.sis()
    elif userinput==3:
        Hotel_Stars.roomrent()
    elif userinput==4:
        Hotel_Stars.dispall()
    elif userinput==5:
        quit()
    else:
        print('Enter your correct choice.')

Menuset()

def runagain():
    runagn=input('\nWant to run again? y/n:')
    while runagn=='y':
        if platform.system=='windows':
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input('\nWant to run again? y/n:')
runagain()
