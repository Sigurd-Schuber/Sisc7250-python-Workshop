a = 200

def flippblipp(a):
    if a%15 == 0:
        return ("flipp blipp")
    elif a%5 == 0:
        return ("blipp")
    elif a%3 == 0:
        return ("flipp")
    else:
        return str(a)

for x in range(1, a+1):
    print (flippblipp (x))