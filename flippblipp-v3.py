def flippblipp(n):
    if n%15 == 0:
        return ("flipp blipp")
    elif n%5 == 0:
        return ("blipp")
    elif n%3 == 0:
        return ("flipp")
    else:
        return str(n)

#n = 200

#for x in range(1, n+1):
#    print (flippblipp (x))

n = 1
print (str(n))

while n < 10:
    print (n)
    n = n+1
    