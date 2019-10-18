import sys
import os
import boto3

def mainMenu():
   os.system('clear')
 


   print ('''
   *********************************************
  		 AWS AUTOMATION SYSTEM MENU
   *********************************************
   ''')
   print ("choose one of the following:")
   print ("1. Instances")
   print ("2. Buckets")
   print ("3. Webserver")
   print ("4. SSH")
   print ("\n0. Quit")

   choice = input(" >>> ")
   if (choice == '1'):
      instanceMenu()
   elif choice =='2':
      bucketMenu()
   elif choice == '3':
      webserverMenu()
   elif choice == '4':
      keysMenu()
   elif choice == '0':
      sys.exit()
   else:
      mainMenu()
   return

import instance

#--------instance Menu-------------

def instanceMenu():
   os.system('clear')
   while True:
     print ('''
     *****************************************************
     			Instance
     *****************************************************
     ''')
     print ("choose from the list of option:")
     print ("1. Create Instance ")
     print ("2. List Instance")
     print ("3. Start Instance")
     print ("4. Stop Instance")
     print ("5. Terminate Instance")
     print ("6. Add Tags")
    

     choice = input(" >>>  ")

     if choice == '1':
      instance.create_instance()
     elif choice == '2':
      instance.list_instance()
     elif choice == '3':
      instance.start_instance()
     elif choice == '4':
      instance.stop_instance()
     elif choice == '5':
      instance.terminate_instance()
     elif choice == '6':
      instance.tags()
     elif choice == '7':
      back()
     elif choice == '0':
      exit()
     else:
      instance_menu()


def main():
   mainMenu()

if __name__ == '__main__':
   main()

