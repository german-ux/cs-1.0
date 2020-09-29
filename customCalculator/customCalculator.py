spd = input("What is your grade in Software Product Developement: ")

if spd == "A" or spd == "a":
    spd = 4
elif spd == "B" or spd == "b":
    spd = 3
elif spd == "C" or spd == "c":
    spd = 2
elif spd == "D" or spd == "d":
    spd = 1
elif spd == "F" or spd == "f":
    spd = 0

cs = input("What is your grade in Copmuter Science: ")

if cs == "A" or cs == "a":
    cs = 4
elif cs == "B" or cs == "b":
    cs = 3
elif cs == "C" or cs == "c":
    cs = 2
elif cs == "D" or cs == "d":
    cs = 1
elif cs == "F" or cs == "f":
    cs = 0

psy = input("What is your grade in Psychology: ")

if psy == "A" or psy == "a":
    psy = 4
elif psy == "B" or psy == "b":
    psy = 3
elif psy == "C" or psy == "c":
    psy = 2
elif psy == "D" or psy == "d":
    psy = 1
elif psy == "F" or psy == "f":
    psy = 0

web = input("What is your grade in Web: ")

if web == "A" or web == "a":
    web = 4
elif web == "B" or web == "b":
    web = 3
elif web == "C" or web == "c":
    web = 2
elif web == "D" or web == "d":
    web = 1
elif web == "F" or web == "f":
    web = 0

GPA = (spd + cs + web + psy)/4

print("Your GPA is: ", GPA)