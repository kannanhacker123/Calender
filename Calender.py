#Calendar Libreary
'''
------------------------------------------------------
                | Created by Kannan |
------------------------------------------------------
'''
import random
import calendar
#pass the year and month and the calendar;
def RandInt(x,y):
    x = random.randint(x,y)
    return x

def print_month():
   x = RandInt(0,7)
   y = RandInt(31,39)
   z = RandInt(41,49)
   
   clrOB = "\033["+str(x)+";"+str(y)+";"+str(z)+"m"
   lastClr = "\033[0;0;0m"
   
   year = int(input(clrOB+"Enter  the year >_ "+lastClr))
   month = int(input(clrOB+'Enter the Month you want to Display \n >_ '+lastClr))
   cal_obj = calendar.month(year,month)  
   #printing the calendar of December 
   
   x = RandInt(0,7)
   y = RandInt(31,39)
   z = RandInt(41,49)
   
   clrOB = "\033["+str(x)+";"+str(y)+";"+str(z)+"m"
   lastClr = "\033[0;0;0m"
   
   print(clrOB+cal_obj+lastClr)


while True:
    try:       
        print_month()
    except:
      
        print("\033[2;31;40m Error \n\033[0;0;0m")     
        pass
        
