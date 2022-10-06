#while Loop


#You are making a game! The player tries to shoot an object and can hit or miss it.
#The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.

#Your program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.

#Sample Input
#hit
#hit
#miss
#hit

#Sample Output
#110

#Explanation: 3 hits add 30 points, one miss deducts 20, making the total points equal to 110.
#Use a while loop to take input during each iteration and calculate the points.


i=-1
x=100
while i<5:
    action=input()
    if action == "hit":
        x=x+10
        i=i+1
    else:
       x=x-20

print(x)







