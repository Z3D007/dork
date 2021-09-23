import os
import time

os.system ("clear")
time.sleep (3)
print ("""\033[0;32m
          1.SQLI DORK List
          2.Developer information
          3.Exit
          """)
print ("")
try:
     a=int(input("select : "))
     if a=="1":
          print ("")
          file=open("sqldork.txt","r")
          print (file.read())
     elif a=="2":
          print ("")
          file=open("developer.txt","r")
          print (file.read())
     else:
          os.system ("clear")
          print ("thanks for use")
          time.sleep (2)
          os.system ("clear")
          exit()
except ValueError:
     print("")
     print ("please 1,2,3 Only Types")
     
          
