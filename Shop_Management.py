"""
Author: Sourabh Shukla
Date: 07-02-2023

"""
import os
import platform
import mysql.connector as s
import datetime
class Shop:
    def __init__(self):
        try:
            self.mydb=s.connect(host="dbpanel.squadinfotech.in",user="testuser",password="testuser",database="testingdb")
            print("Connected to Mysql")
            
        except:
            print("Not connected")

        #creating tables
        self.Grocery_shop="create table if not exists Grocery_shop(product_name varchar(20),product_price varchar(20),product_quantity varchar(20),product_number varchar(10))"
        self.Order_shop="create table if not exists Order_shop(custno varchar(25),order_pno varchar(10),order_pqt varchar(10),bill_total varchar(10))"
        
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute(self.Grocery_shop)
        self.mycursor.execute(self.Order_shop)
        self.mydb.commit()
         
    def add_product(self):
        L=[]
        product_name=(input('Enter a Item Name :'))
        L.append(product_name)
        product_price=input('Enter product_price :')
        L.append(product_price)
        Quantity=input('Enter quantity:')
        L.append(Quantity)
        product_number=input("Enter the product number: ")
        L.append(product_number)
        print("product added sucessfully")        
        product=(L)
        sql='insert into Grocery_shop(product_name,product_price,product_quantity,product_number) values(%s,%s,%s,%s)'
        self.mycursor.execute(sql,product)
        self.mydb.commit()
    
    def delete_product(self):
        prod_name=input("Enter product name  :")
        sql="delete from Grocery_shop where product_name=%s"
        rl=(prod_name,)
        self.mycursor.execute(sql,rl)
        print("Deleted product successfully.....!!") 
    
    def view_products(self):  
        sql="Select * from Grocery_shop"   
        self.mycursor.execute(sql)
        res=self.mycursor.fetchall()
        print("Product-Name  Price  Quantity  Product_id")
        for x in res:
            print(f"{x[0]}           {x[1]}      {x[2]}        {x[3]} ") 
    
    def view_products_consumer(self):  
        sql="Select * from Grocery_shop"   
        self.mycursor.execute(sql)
        res=self.mycursor.fetchall()
        print("Product-Name  Price")
        for x in res:
            print(f"{x[0]}           {x[1]} ") 
        
    def Order_product(self):
        L=[]
        cust_name=(input('Enter your name :'))
        L.append(cust_name)
        order_pno=input('Enter product name :')
        L.append(order_pno)
        order_pqt=input('Enter quantity:')
        L.append(order_pqt)
        print("Order added sucessfully to deliver")    
        sql="Select * from Grocery_shop where Grocery_shop.product_name=%s"
        rl=(order_pno,)
        self.mycursor.execute(sql,rl)
        res=self.mycursor.fetchall()
        bill=0
        for x in res:
            print(x[1])
            bill+=int(order_pqt) * int(x[1])
        L.append(bill)     
        ord=(L)
        sql='insert into Order_shop(custno,order_pno,order_pqt,bill_total) values(%s,%s,%s,%s)'
        self.mycursor.execute(sql,ord)
        self.mydb.commit()
    
    def Total_bill(self):
        c=input("Whose bill do you want to check? Enter Your name:")
        sql="Select * from Order_shop"   
        self.mycursor.execute(sql)
        res=self.mycursor.fetchall()
        for x in res:
            if x[0]==c:
                print(f"{x[0]} your total bill is M.R.P={x[3]}")
            else:
                continue

    def Cancel_order(self):
        order_name=input("Enter Movie name  :")
        sql="delete from myshows where Moviename=%s"
        rl=(order_name,)
        self.mycursor.execute(sql,rl)
        print("Delete show successfully.....!!")
                                                                                         
   
        
Star_Shop=Shop()


def Menuset():
    b=input(("Do you want to open the owner side or user side?\nEnter 'o' for owner side and 'u' for user side "))
    if b =='o':
        print("---Welcome to Admin Side---\nHere are the following functions you can perform")

        print('Enter 1: To add a product.\n2: delete a product.\n3.View all Your Products and their data')
        useri=(input("Enter Your requirement"))
        print(useri)
        try:
            if useri=='1':
                Star_Shop.add_product()
            if useri=='2':
                Star_Shop.delete_product()
            if useri=='3':
                Star_Shop.view_products()
        except:
            print("You have entered a wrong input")

    elif b=="u":
        print("Welcome to User side---\nHere are the following functions you can perform")
        print('Enter 1: View all Products and their prices .\n2: Order a product.\n3.Check your total bill\n4. Cancel Your order')
        useri=int(input("Enter Your requirement"))
        try:
            if useri==1:
                Star_Shop.view_products_consumer()
            elif useri==2:
                Star_Shop.Order_product()
            elif useri==3:
                Star_Shop.Total_bill()
            elif useri==4:
                Star_Shop.Cancel_Order()
        except:
            print("You have entered a wrong input")
    # elif userinput==4:
    #     Star_Shop.dispall()
    # elif userinput==5:
    #     quit()
    # else:
    #     print('Enter correct choice.')
Menuset()

def runagain():
    runagn=input('\nWant to run again? y/n:')
    # while runagn=='y':
    if runagn=="y":
    # if platform.system=='windows':
        Menuset()
        # print(os.system('cls'))
    else:
        exit()
        print(os.system('clear'))
    # Menuset()
runagain()
