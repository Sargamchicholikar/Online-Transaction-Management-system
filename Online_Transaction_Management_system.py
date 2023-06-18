




import mysql.connector
from prettytable import PrettyTable

# GLOBAL VARIABLES DECLARATION

myConnnection =""
cursor=""
userName=""
password =""
email_addr = ""


#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck():
 global myConnection
 global userName
 global password
 
 myConnection=mysql.connector.connect(host="localhost",user="root" ,passwd = "123456" )
 if myConnection:
   cursor=myConnection.cursor()
   cursor.execute("CREATE DATABASE IF NOT EXISTS ACCOUNTMANAGEMENT")
   myConnection.commit()
   cursor.close()
   return myConnection
 else:
   print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")  

#MODULE TO ESTABLISH MYSQL CONNECTION
def MYSQLconnection ():
     global userName
     global password
     global myConnection
 
     myConnection=mysql.connector.connect(host="localhost",user = "root" , passwd = "123456" ,  database="ACCOUNTMANAGEMENT" )
     if myConnection:
         return myConnection
     else:
         print("\nERROR ESTABLISHING MYSQL CONNECTION !")
         myConnection.close()





# MODULE TO CREATE NEW USER/sign up

def SIGNUP():
   if myConnection:
      cursor=myConnection.cursor()
      createTable ="CREATE TABLE IF NOT EXISTS LOGIN (NAME VARCHAR(30) NOT NULL,email_id varchar(50)not null ,passwd varchar(12)not null unique)"
      cursor.execute(createTable)
      print("\nPlease Fill All The Information Carefully !")
      name=str(input("Please Enter Name : "))
      email_id=str(input("Please Enter email id : "))
      passwd=str(input("Please Enter password :"))
      sql="INSERT INTO LOGIN VALUES(%s,%s,%s)"
      values =(name,email_id,passwd)
      cursor.execute(sql,values)
      myConnection.commit()
      cursor.close()
      print("\nNew Successfully sign up done !")    


    
# MODULE log in user

def LOGIN():
   if myConnection:  
     cursor=myConnection.cursor()
     email_id=str(input("Please Enter your email id : "))
     passwd=str(input("PLEASE ENTER your password : "))
     sql=("SELECT COUNT(*) FROM LOGIN WHERE email_id LIKE %s and passwd LIKE %s")
     values =(email_id,passwd)
     cursor.execute(sql,values)
     data = cursor.fetchone()
     if data and data[0] == 1:
         global email_addr
         email_addr = email_id
         print("\n Successfully Log In Done ! ", email_addr)
     else:
         print("\n  SIGN UP  !")
   
     

# MODULE TO CREATE DETAILS
def  DETAILS():
    if myConnection:
        cursor=myConnection.cursor()
        createTable="CREATE TABLE IF NOT EXISTS DETAILS(ID VARCHAR(10) NOT NULL UNIQUE,NAME VARCHAR(50)NOT NULL,ADDRESS VARCHAR(50)NOT NULL,PHONE VARCHAR(12) NOT NULL,ACCOUNT_NO varchar(20) NOT NULL UNIQUE,EMAIL_ID VARCHAR(50)NOT NULL)"
        cursor.execute(createTable)
        id=str(input("PLEASE ENTER YOUR ID :"))
        name=str(input("PLEASE ENTER YOUR NAME : "))
        address=str(input("PLEASE ENTER YOUR ADDRESS : "))
        phone=str(input("Please Enter your Contact No. : "))
        account_no=str(input("PLEACE ENTER YOUR ACCOUNT NO. : "))
        email_id=str(input("PLEASE ENTER YOUR EMAIL ID : "))
        sql="INSERT INTO DETAILS VALUES(%s,%s,%s,%s,%s,%s)"
        values=(id,name,address,phone,account_no,email_id)
        cursor.execute(sql,values)
        myConnection.commit()
        cursor.close()
        print("\n Successful")



        
# MODULE TO VIEW DETAILS    

def VIEWDETAILS():
    myConnection = MYSQLconnectionCheck ()
    if myConnection:
        MYSQLconnection ()
        while(1):

            print("\n!===============VIEW DETAILS================!")
            print(" 1 for personal details ")
            print(" 2 for account details ")
            print(" 3 for tarsection detals ")
            print(" 4 for menu ")
            print("\n!=========================*************=======================!")
            choice= int(input("\n Please Enter Your Choice : "))
            if choice == 1:
                PERSONALDETAILS()
            elif choice == 2:
                ACCOUNTDETAILS()
            elif choice == 3:
                TARSECTIONDETAILS()
            elif choice == 4:
                MENU()
                break



# MODULE TO VIEW PERSONAL DETAILS
def PERSONALDETAILS():
   if myConnection:  
     cursor=myConnection.cursor()
     id=str(input("Please Enter  ID : "))
     sql="SELECT * FROM DETAILS WHERE ID = %s"
     values =(id,)
     cursor.execute(sql,values)
     data = cursor.fetchall()
     t = PrettyTable(["ID"," NAME","ADDRESS","PHONE","ACCOUNT_NO","EMAIL"])
     if data:
          for i in data:
               a,b,c,d,e,f = i
               t.add_row([a,b,c,d,e,f])
          print(t)     
     else:
          print("Sorry ! No Record Found , Please Try Again ! ")
   else:
     print("\nERROR ESTABLISHING MYSQL CONNECTION !")                                       


            
# MODULE TO VIEW DEPOSIT DETAILS
def DEPOSITDETAILS():
   if myConnection:  
     cursor=myConnection.cursor()
     id=str(input("Please Enter  ACCOUNT_NO. : "))
     sql="SELECT * FROM DEPOSIT WHERE ACCOUNT_NO = %s"
     values =(id,)
     cursor.execute(sql,values)
     data = cursor.fetchall()
     t = PrettyTable(["ACCOUNT_NO"," moneydeposit","totalbalance","newbalance"])
     if data:
          for i in data:
               a,b,c,d = i
               t.add_row([a,b,c,d])
          print(t)     
     else:
          print("Sorry ! No Record Found , Please Try Again ! ")
   else:
     print("\nERROR ESTABLISHING MYSQL CONNECTION !")                                       


# MODULE TO VIEW WITHDRAW DETAILS
def WITHDRAWDETAILS():
   if myConnection:  
     cursor=myConnection.cursor()
     id=str(input("Please Enter  ACCOUNT_NO. : "))
     sql="SELECT * FROM WITHDRAW WHERE ACCOUNT_NO = %s"
     values =(id,)
     cursor.execute(sql,values)
     data = cursor.fetchall()
     t = PrettyTable(["ACCOUNT_NO"," moneywithdraw","totalbalance","newbalance"])
     if data:
          for i in data:
               a,b,c,d = i
               t.add_row([a,b,c,d])
          print(t)     
     else:
          print("Sorry ! No Record Found , Please Try Again ! ")
   else:
     print("\nERROR ESTABLISHING MYSQL CONNECTION !")                                       


# MODULE TO VIEW TARSECTION DETAILS
def TARSECTIONDETAILS():
    myConnection = MYSQLconnectionCheck ()
    if myConnection:
        MYSQLconnection ()
        while(1):

            print("\n!===============VIEW DETAILS================!")
            print(" 1 for deposit details ")
            print(" 2 for withdraw details ")
            print(" 3 for view details ")
            print("\n!=========================*************=======================!")
            choice= int(input("\n Please Enter Your Choice : "))
            if choice == 1:
                DEPOSITDETAILS()
            elif choice == 2:
                WITHDRAWDETAILS()
            elif choice == 3:
                VIEWDETAILS()
                break


    
# MODULE TO CREATE ACCOUNT

def CREATEACCOUNT():
    if myConnection:
        cursor=myConnection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS ACCOUNT ( ID varchar(15) NOT NULL UNIQUE,ACCOUNT_NO INT(15) NOT NULL UNIQUE,ACCOUNT_TYPE VARCHAR(15) NOT NULL,ACCOUNT_PIN VARCHAR(6) NOT NULL UNIQUE)"
        cursor.execute(createTable)
        ID=str(input("PLEASE ENTER THE ID  : "))
        ACCOUNT_NO=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
        account_type=str(input("PLEASE ENTER THE ACCOUNT TYPE [ SAVING / CURRENT ] : "))
        account_pin=str(input("PLEASE ENTER THE ACCOUNT PIN : "))
        sql="INSERT INTO ACCOUNT VALUES (%s,%s,%s,%s)"
        values =(ID,ACCOUNT_NO,account_type,account_pin)
        cursor.execute(sql,values)
        myConnection.commit()
        print("\nNew Account Opened Successfully !")
    else:
            print("\n GIVEN DATA IS NOT UNIQUE ! ")
            
        

# MODULE TO VIEW ACCOUNT DETAILS
def ACCOUNTDETAILS():
   if myConnection:  
     cursor=myConnection.cursor()
     id=str(input("Please Enter  ID : "))
     sql="SELECT * FROM ACCOUNT WHERE ID = %s"
     values =(id,)
     cursor.execute(sql,values)
     data = cursor.fetchall()
     t = PrettyTable([" ID","ACCOUNT_NO","ACCOUNT_TYPE","ACCOUNT_PIN"])
     if data:
          for i in data:
               a,b,c,d = i
               t.add_row([a,b,c,d])
          print(t)     
     else:
          print("Sorry ! No Record Found , Please Try Again ! ")
   else:
     print("\nERROR ESTABLISHING MYSQL CONNECTION !")



        

# MODULE TO MONEY DEPOSIT

def DEPOSIT():
    if myConnection:
        cursor=myConnection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS DEPOSIT ( ACCOUNT_NO INT(15) NOT NULL, MONEYDEPOSIT INT(50) default 0, TOTALBALANCE INT(50) default 0, NEWBALANCE INT(50))"
        cursor.execute(createTable)
        ACCOUNT_NO = int(input("PLEASE ENTER THE ACCOUNT_NO : "))
        sql=("SELECT COUNT(*) FROM ACCOUNT WHERE ACCOUNT_NO = %s")
        values =(ACCOUNT_NO,)
        cursor.execute(sql,values)
        data = cursor.fetchone()
        if data and data[0] == 1:
            totalbalance=int(input("PLEASE ENTER TOTAL BALANCE :"))
            moneydeposit=int(input("PLEASE ENTER AMOUNT TO DEPOSIT : "))
            newbalance = moneydeposit + totalbalance
            sql="INSERT INTO DEPOSIT VALUES(%s,%s,%s,%s)"
            values=(ACCOUNT_NO,moneydeposit,totalbalance,newbalance)
            cursor.execute(sql,values)
            myConnection.commit()
            print("******* deposit SUCCESSFULLY COMPLETED ! *******")
        else:
            print("Sorry ! No Record Found , Please Try Again ! ")

# MODULE TO WITHDRAW  

def WITHDRAW():
    count =3
    if myConnection:
        cursor=myConnection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS WITHDRAW ( ACCOUNT_NO INT(15) NOT NULL, MONEYWITHDRAW INT(50) default 0, TOTALBALANCE INT(50) default 0, NEWBALANCE INT(50))"
        cursor.execute(createTable)
        ACCOUNT_NO=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
        sql=("SELECT * FROM DEPOSIT WHERE ACCOUNT_NO = %s")
        values =(ACCOUNT_NO,)
        cursor.execute(sql,values)
        data = cursor.fetchone()
        if data:
            while True:
                ACCOUNT_PIN=int(input("PLEASE ENTER THE ACCOUNT PIN - ONLY 3 ATTEMPTS ARE ALLOWED : "))
                sql='SELECT COUNT(*) FROM ACCOUNT WHERE ACCOUNT_PIN = %s'
                values =(ACCOUNT_PIN,)
                cursor.execute(sql,values)
                data1 = cursor.fetchone()
                if data1 and data1[0] == 1:
                    WITHDRAW_AMOUNT=int(input("PLEASE ENTER AMOUNT TO WITHDRAW : "))
                    sql="INSERT INTO WITHDRAW VALUES(%s,%s,%s,%s)"
                    newbalance = data[3] - WITHDRAW_AMOUNT
                    values=(ACCOUNT_NO,WITHDRAW_AMOUNT,data[3],newbalance)
                    cursor.execute(sql,values)
                    myConnection.commit()
                    print("******* TRANSACTION SUCCESSFULLY COMPLETED ! *******")
                    break
                else:
                    print("Wrong Pin ! Please enter a Valid PIN")
                    count=count-1
                    print("You are left with only ",count ,"Attempts")
                    if count == 0:
                        print("Your Card has been Blocked , Please Visit the Branch to activate it")
                        break
    else:
        print("Sorry ! Account Infromation NOT Found , Please Try Again ! ")


    
        
# MODULE FOR UPDATE
def UPDATE():
    myConnection = MYSQLconnectionCheck ()
    if myConnection:
        MYSQLconnection ()
        while(1):
            
            print("\n!=======UPDATE=========!")
            print(" 1 for name ")
            print(" 2 for phone ")
            print(" 3 for email ")
            print(" 4 for password ")
            print(" 5 for update all ")
            print(" 6 for menu ")
            print("\n!=========*****========!")
            choice= int(input("\n Please Enter Your Choice : "))
            if choice == 1:
                name()
            elif choice == 2:
                phone()
            elif choice == 3:
                email()
            elif choice == 4:
                password()
            elif choice == 5:
                updateall()
            elif choice == 6:
                MENU()
                break

# MODULE FOR UPDATE NAME
def name():
    if myConnection:
        cursor=myConnection.cursor()
        old_name=str(input(" ENTER OLD NAME : "))
        new_name=str(input(" ENTER NEW NAME : "))
        sql="UPDATE DETAILS SET NAME=%s WHERE NAME=%s"
        value=(new_name,old_name)
        cursor.execute(sql,value)
        myConnection.commit()
        print("\n Successfully Update !")



# MODULE FOR UPDATE EMAIL
def email():
    if myConnection:
        cursor=myConnection.cursor()
        old_email=str(input(" ENTER OLD Email : "))
        new_email=str(input(" ENTER NEW Email : "))
        sql="UPDATE DETAILS SET EMAIL_ID=%s WHERE EMAIL_ID=%s"
        value=(new_email,old_email)
        cursor.execute(sql,value)
        myConnection.commit()
        print("\n Successfully Update !")


# MODULE FOR UPDATE PHONE
def phone():
    if myConnection:
        cursor=myConnection.cursor()
        old_phone=str(input(" ENTER OLD PHONE : "))
        new_phone=str(input(" ENTER NEW PHONE : "))
        sql="UPDATE DETAILS SET PHONE=%s WHERE PHONE=%s"
        value=(new_phone,old_phone)
        cursor.execute(sql,value)
        myConnection.commit()
        print("\n Successfully Update !")

# MODULE FOR UPDATE PASSWORD
def password():
    if myConnection:
        cursor=myConnection.cursor()
        old_password=str(input(" ENTER OLD PASSWORD : "))
        new_password=str(input(" ENTER NEW PASSWORD : "))
        sql="UPDATE LOGIN SET passwd=%s WHERE passwd=%s"
        value=(new_password,old_password)
        cursor.execute(sql,value)
        myConnection.commit()
        print("\n Successfully Update !")

# MODULE FOR UPDATE ALL
def updateall():
    if myConnection:
        cursor=myConnection.cursor()
        old_name=str(input(" ENTER OLD NAME           : "))
        new_name=str(input(" ENTER NEW NAME           : "))
        new_phone=str(input(" ENTER NEW PHONE        : "))
        new_email=str(input(" ENTER NEW EMAIL        : "))
        sql="UPDATE DETAILS SET NAME=%s,PHONE=%s,EMAIL_ID=%s WHERE NAME=%s"
        value=(new_name,new_phone,new_email,old_name)
        cursor.execute(sql,value)
        myConnection.commit()
        print("\n Successfully Update !")




# MODULE logout in user
def LOGOUT():
   if myConnection:  
     cursor=myConnection.cursor()
     sql="DELETE FROM LOGIN WHERE email_id=%s"
     global email_addr
     value=(email_addr,)
     cursor.execute(sql,value)
     myConnection.commit()
     print("\n Successfully Logout Done ! ", email_addr)

    
# MODELU FOR  MENU SCREEN
def MENU():
    myConnection = MYSQLconnectionCheck ()
    if myConnection:
        MYSQLconnection ()
        while(1):

            print("\n!==============MENU================!")
            print(" 1 for VIEW DETAILS ")
            print(" 2 for CREATE NEW ACCOUNT ")
            print(" 3 for DEPOSIT ")
            print(" 4 for WITHDRAW ")
            print(" 5 for UPDATE ")
            print(" 6 for LOGOUT ")
            print("\n!============*********=============!")
            choice= int(input("\n Please Enter Your Choice : "))
            if choice == 1:
                VIEWDETAILS()
            elif choice == 2:
                CREATEACCOUNT()
            elif choice == 3:
                DEPOSIT()
            elif choice == 4:
                WITHDRAW()
            elif choice == 5:
                UPDATE()
            elif choice == 6:
                LOGOUT()
                break


#STARTING POINT OF THE SYSTEM

myConnection = MYSQLconnectionCheck ()
if myConnection:
    MYSQLconnection ()
    while(1):
       print("\n!========WELCOME========!") 
       print("\n!MANAGE YOUR ACCOUNT PERSONALY !")  
       print("! PLEASE ENTER 1 TO SIGNUP !")
       print("! PLEASE ENTER 2 TO LOGIN !")
       print("! PLEASE ENTER 3 TO PERSONAL DETAILS !")
       print("! PLEASE ENTER 4 TO MENU SCREEN !")
       print("\n!==========END==========!")
       choice = int(input("\n Please Enter Your Choice : "))
       if choice == 1:
          SIGNUP()
       elif choice == 2:
           LOGIN()
       elif choice == 3:
           DETAILS()
       elif choice == 4:
           MENU()
           break


        

     

#(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

#(" T  H  A  N  K ")
#(" Y  O  U ")

#(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")  

# END OF THE PROJECT








