x = 0
while x <= 100000:
    if x % 2 == 0:
        print(str(x) + " is even")
    elif not (x % 2 == 0):
        print(str(x) + " is odd")
    x += 100
