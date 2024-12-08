# ---------------------- HOTEL MANAGEMENT SYSTEM ---------------------
# --------------------------- AVANTI HOTELS --------------------------


'''Designed and Maintained By :
"Avantika Chauhan - 2020-2021" '''

import mysql.connector

#Declaration of global variables
myConnnection =""
cursor=""
username=""
password =""
roomrent = 0
restaurantbill = 0
grandTotal= 0
cid = ""

# MODULE TO CHECK  MYSQL CONNECTIVITY

def MYSQLconnectionCheck():
    global myConnection
    global username
    global password
    username = input("\nENTER MYSQL SERVER'S USERNAME: ")
    password = input("\nENTER MYSQL SERVER'S PASSWORD : ")
    myConnection = mysql.connector.connect(host="localhost", user=username, passwd=password, auth_plugin='mysql_native_password')
    if myConnection:
        print("\nCONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor = myConnection.cursor()
        cursor.execute("Create database if not exists avanti_hotels;")
        cursor.execute("Commit")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

#MODULE TO ESTABLISH MYSQL CONNECTION

def MYSQLconnection ():
    global username
    global password
    global myConnection
    global cid
    myConnection=mysql.connector.connect(host="localhost", user=username, passwd=password, database="avanti_hotels",
                                         auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()

def userEntry():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        createTable="CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))"
        cursor.execute(createTable)
        cid = input("Enter Customer Identification Number  :  ")
        name = input("Enter Customer Name  :  ")
        address = input("Enter Customer Address  : ")
        age= input("Enter Customer Age  : ")
        nationality = input("Enter Customer Country  :  ")
        phoneno= input("Enter Customer Contact Number  :  ")
        email = input("Enter Customer Email  :  ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values= (cid,name,address,age,nationality,phoneno,email)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nNew Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


def bookingRecord():
    global cid
    customer=searchCustomer()
    if customer:
     if myConnection:
        cursor=myConnection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE);"
        cursor.execute(createTable)
        checkin=input("\nEnter Customer CheckIN Date [ YYYY-MM-DD ]  :   ")
        checkout=input("\nEnter Customer CheckOUT Date [ YYYY-MM-DD ]  :   ")
        sql= "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s);"
        values= (cid,checkin,checkout)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nCHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
        cursor.close()
    else:
      print("\nERROR ESTABLISHING MYSQL CONNECTION !")


def roomRent():
    global cid
    customer=searchCustomer()
    if customer:
        global roomrent
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)"
            cursor.execute(createTable)
            print ("\n ##### We have The Following Rooms For You #####")
            print (" 1. Ultra Royal ----> 10000 Rs.")
            print (" 2. Royal ----> 5000 Rs. ")
            print (" 3. Elite ----> 3500 Rs. ")
            print (" 4. Budget ----> 2500 Rs. ")
            roomchoice =int(input("Enter Your Option : "))
            roomno=int(input("Enter Customer Room No : "))
            noofdays=int(input("Enter No. Of Days : "))
            if roomchoice==1:
                roomrent = noofdays * 10000
                print("\nUltra Royal Room Rent : ",roomrent)
            elif roomchoice==2:
                roomrent = noofdays * 5000
                print("\nRoyal Room Rent : ",roomrent)
            elif roomchoice==3:
                roomrent =noofdays * 3500
                print("\nElite Royal Room Rent : ",roomrent)
            elif roomchoice==4:
                roomrent = noofdays * 2500
                print("\nBudget Room Rent : ",roomrent)
            else:
                print("Sorry, Invalid input, Please Try Again ! ")
                return
            sql="INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
            values= (cid,roomchoice,noofdays,roomno,roomrent,)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("Thank You , Your Room Has Been Booked For : ",noofdays , "Days" )
            print("Your Total Room Rent is : Rs. ",roomrent)
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def Restaurant():
     global cid
     customer=searchCustomer()
     if customer:
         global restaurantbill
         if myConnection:
             cursor=myConnection.cursor()
             createTable="""CREATE TABLE IF NOT EXISTS RESTAURANT(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"""
             cursor.execute(createTable)
             print("1. North Indian Thali -----> 300 Rs.")
             print("2. South Indian Thali -----> 500 Rs.")
             print("3. Chinese Combo -----> 550 Rs.")
             print("4. Italian Combo -----> 600 Rs.")
             print("5. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")

             choice_dish= int(input("Enter Your Cuisine : "))
             quantity = int(input("Enter Quantity : "))
             if choice_dish == 1:
                 print("\nSO YOU HAVE ORDER: North Indian Thali ")
                 restaurantbill = quantity * 300
             elif choice_dish == 2:
                 print("\nSO YOU HAVE ORDER: South Indian Thali ")
                 restaurantbill = quantity * 500
             elif choice_dish == 3:
                 print("\nSO YOU HAVE ORDER: Chinese Combo ")
                 restaurantbill = quantity * 550
             elif choice_dish == 4:
                 print("\nSO YOU HAVE ORDER: Italian Combo ")
                 restaurantbill = quantity * 600
             elif choice_dish == 5:
                 print("\nSO YOU HAVE ORDER: Vegetarian & Non-Vegetarian Combo ")
                 restaurantbill = quantity * 750
             else:
                 print("Sorry, Invalid input, Please Try Again ! ")
                 return
             sql = "INSERT INTO restaurant VALUES(%s,%s,%s,%s)"
             values = (cid, choice_dish, quantity, restaurantbill)
             cursor.execute(sql, values)
             cursor.execute("COMMIT")
             print("Your Total Bill Amount Is : Rs. ", restaurantbill)
             print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n")
             cursor.close()
     else:
         print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def totalAmount():
    global cid
    customer=searchCustomer()
    if customer:
        global grandTotal
        global roomrent
        global restaurantbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20),C_NAME VARCHAR(30),ROOMRENT INT ,RESTAURANTBILL INT ,TOTALAMOUNT INT)"
            cursor.execute(createTable)
            sql="INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s)"
            name = input("Enter Customer Name : ")
            grandTotal=roomrent+restaurantbill
            values=(cid,name,roomrent,restaurantbill,grandTotal)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            cursor.close()
            print("\n **** AVANTI HOTELS **** CUSTOMER BILLING ****")
            print("\n CUSTOMER NAME : ",name)
            print("\nROOM RENT : Rs. ",roomrent)
            print("\nRESTAURANT BILL : Rs. ",restaurantbill)
            print("___________________________________________________")
            print("\nTOTAL AMOUNT : Rs. ",grandTotal)
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def OldBill():
    global cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            sql="SELECT * FROM TOTAL WHERE CID= %s"
            cursor.execute(sql,(cid,))
            data=cursor.fetchall()
            if data:
                print(data)
            else:
                print("Record Not Found Try Again !")
                cursor.close()
    else:
        print("\nsomething Went Wrong ,Please Try Again !")

def searchCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("ENTER CUSTOMER ID : ")
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql,(cid,))
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print("Record Not Found Try Again !")
            return False
        cursor.close()
    else:
        print("\nsomething Went Wrong ,Please Try Again !")


print("""---------------------- HOTEL MANAGEMENT SYSTEM ---------------------
--------------------------- AVANTI HOTELS -----------------------------
Designed and Maintained By :
Avantika Chauhan - CLASS XII A - ROLL NO - 9 [ 2020-2021 ]""")

myConnection = MYSQLconnectionCheck()
if myConnection:
    MYSQLconnection()
    while True:
        print("""
        1--->Enter Customer Details
        2--->Booking Record
        3--->Calculate Room Rent
        4--->Calculate Restaurant Bill
        5--->Display Customer Details
        6--->GENERATE TOTAL BILL AMOUNT
        7--->GENERATE OLD BILL
        8--->EXIT """)
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            userEntry()
        elif choice == 2:
            bookingRecord()
        elif choice == 3:
            roomRent()
        elif choice == 4:
            Restaurant()
        elif choice == 5:
            searchCustomer()
        elif choice == 6:
            totalAmount()
        elif choice == 7:
            OldBill()
        elif choice == 8:
            break
        else:
            print("Sorry, Invalid input, Please Try Again ! ")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION !")
