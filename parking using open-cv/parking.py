# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:49:46 2019

@author: Saket Mishra
"""

import os
import sys
import time
import capture
#install termcolor module or else you will get import error
#For blink effect use xterm
from termcolor import colored

car_parking=['available','available','available','available','available']
bike_parking=['available','available','available']
localtime = time.asctime( time.localtime(time.time()) )

while True:
   button_press=input(colored("""Library parking
Total slots for car is 5 and bike is 3
Press button a for car parking 
Press button b for bike parking 
Press button e for exit 
--------->> """,'blue'))
   
   if button_press == 'a':
      for i in car_parking:
         if i == 'available':
			
            print ("			","     ",colored(i , 'green',attrs=['reverse', 'blink']))
            z=(car_parking.index(i))
            sum=z+1
            print("			","Your slot number is", str(sum)+'c'  )
            print("			",localtime)
            print("			"," ",colored("please take right",'green',attrs=['reverse', 'blink']))
            capture.park()
            car_parking[z]='false'
            time.sleep(5)
            os.system('clear')
            break
      else:
          print("			",colored('Sorry! No space available. Park outside.','red',attrs=['reverse', 'blink']))
          time.sleep(5)
          os.system('clear')

   elif button_press =='b':
      for i in bike_parking:
         if i == 'available':
			
            print ("			","     ",colored(i , 'red',attrs=['reverse', 'blink']))
            z=(bike_parking.index(i))
            sum=z+1
            print("			","Your slot number is", str(sum)+'b'  )
            print("			",localtime)
            print("			"," ",colored("please take right",'red',attrs=['reverse', 'blink']))
            capture.park()
            bike_parking[z]='false'
            time.sleep(5)
            os.system('clear')
            break
      else:
          print("			",colored('Sorry! No space available.Park outside.','red',attrs=['reverse', 'blink']))
          time.sleep(5)
          os.system('clear')
          
   else:
      check=input(" \n   Enter slot number :")
      if check == '1c':
         if car_parking[0]=='false':
             car_parking[0]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')   
      elif check == '2c':
         if car_parking[1]=='false':
             car_parking[1]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')      
      elif check == '3c':
         if car_parking[2]=='false':
             car_parking[2]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')
      elif check == '4c':
         if car_parking[3]=='false':
             car_parking[3]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')
      elif check == '5c':
         if car_parking[4]=='false':
             car_parking[4]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')
      elif check == '1b':
         if bike_parking[0]=='false':
             bike_parking[0]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')
      elif check == '2b':
         if bike_parking[1]=='false':
             bike_parking[1]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')
      elif check == '3b':
         if bike_parking[2]=='false':
             bike_parking[2]='available' 
             print("				",colored("Bye!",'red',attrs=['reverse', 'blink']))
             print("			",localtime)
             time.sleep(3)
             os.system('clear')
         else :
            print("\n","		",colored("You've entered wrong slot number",'red',attrs=['reverse', 'blink']))
            time.sleep(3)
            os.system('clear')
      else :
         print("         		",colored("wrong slot",'red',attrs=['reverse', 'blink']))            
         time.sleep(3)
         os.system('clear')
