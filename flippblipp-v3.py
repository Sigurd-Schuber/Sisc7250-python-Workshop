def flippblipp(a):
    if a%15 == 0:
        return ("flipp blipp")
    elif a%5 == 0:
        return ("blipp")
    elif a%3 == 0:
        return ("flipp")
    else:
        return str(a)

n = 1
print("      ", n)
state = True

while state == True:
    n = n+1
    korrekt = flippblipp(n)
    inm = input("Nästa: ")
    if inm != korrekt:
        state = False
        print("Fel - ", korrekt)
        print()
        print("Game Over")
