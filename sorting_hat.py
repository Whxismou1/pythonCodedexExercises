Hufflepuff = 0
Slytherin = 0
Gryffindor = 0
Ravenclaw = 0

print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")

answer1 = int(input("What's your answer (1 or 2): "))
if answer1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer1 == 2:
    Hufflepuff +=1
    Slytherin +=1
else:
    print("Wrong input!")

print("*********************************************")

print("Q2) When I´m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")

answer2 = int(input("What's your answer (1, 2, 3 or 4): "))
if answer2 == 1:
    Hufflepuff += 1
elif answer2 == 2:
    Slytherin+=1
elif answer2 == 3:
    Ravenclaw += 1
elif answer2 == 4:
    Gryffindor += 1
else:
    print("Wrong input!")

print("*********************************************")

print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer3 = int(input("What's your answer (1, 2, 3 or 4): "))

if answer3 == 1:
    Slytherin += 1
elif answer3 == 2:
    Hufflepuff+=1
elif answer3 == 3:
    Ravenclaw += 1
elif answer3 == 4:
    Gryffindor += 1
else:
    print("Wrong input!")

print("*********************************")
print("Gryffindor: ", Gryffindor )
print("Slytherin", Slytherin)
print("Hufflepuff", Hufflepuff)
print("Ravenclaw: ", Ravenclaw)
print("*********************************")

max_Points = max(Gryffindor, Slytherin, Hufflepuff, Ravenclaw)

if max_Points == Gryffindor:
    print("🦁 Gryffindor")
if max_Points == Ravenclaw:
    print("🦅 Ravenclaw")
if max_Points == Hufflepuff:
    print("🦡 Hufflepuff")
if max_Points == Slytherin:
    print("🐍 Slytherin")