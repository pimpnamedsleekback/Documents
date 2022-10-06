#purity = float(input())
#if ( 91.7 <=purity<= 99.9):
    #print("Accepted")
#else: print("Rejected!")




 #If, elif & else conditions.
#price = 60
#if price > 100:
    #print("price is greater than 100")
#elif price == 100:
     #print("price is 100")
#else:
   #if price < 100:
     #print("price is less than 100")
    #Output: Price is less than 100

#year = int(input())
#if year % 4==0:
    #if year % 100==0:
       #if year % 400==0:
           #print("leap year")
#else:
    #print("Not leap year")
#To check whether a year is a leap year or not, you need to check the following:
#1) If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
#2) If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
#3) If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a leap year.


year = int(input())
if year % 4 != 0:
    print("Not a leap year")
elif year % 100 != 0:
    print("leap year")
elif year % 400 == 0:
    print("leap year")
elif year % 400 !=0:
    print("Not leap year")

if year % 400 == 0:
    print ("Leap year")
elif year % 100 == 0:
    print ("Not a leap year")
elif year % 4 == 0:
    print ("Leap year")
else: print ("Not a leap year")

#int(input())
#your code goes here
#if year % 4 != 0: # not divisible by 4
     #print("Not a leap year")
#elif year % 100 != 0: # not divisible by 100
     #print("Leap year")
 #elif year % 400 == 0: # divisible by 400 print("Leap year")
 #else: # any other
  #print("Not a leap year")



purity = float(input())
if 75<=purity<=83.2:
    print("18K")
elif 83.3<=purity<=91.6:
    print("20K")
elif 91.7<=purity<=99.8:
    print("22K")
else:
    print("24K")


#age = 15
#Money = 500
if age > 18 or Money > 100:
    print("Age is nothing money is everything!")

x = 1
while x < 10:
  if (x % 2 == 0):
    print(str(x) + " is even")
  elif not(x % 2 == 0):
    print(str(x) + " is odd")
  x+= 1


