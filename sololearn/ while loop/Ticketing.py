#You are making a ticketing system.
#The price of a single ticket is $100.
#For children under 3 years old, the ticket is free.

#Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

#Sample Input
#18
#24
#2
#5
#42

#Sample Output
#400


total=0
i=0
while i<3:
    age = int(input())
    i=i+1
    if age < 3:
        continue
    total +=100
print(total)