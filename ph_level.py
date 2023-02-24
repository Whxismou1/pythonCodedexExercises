ph = int(input("Enter a pH between 0-14: "))

if ph > 7:
    print("Basic pH")
elif ph <7:
    print("Acidic pH")
else:
    print("Neutral pH")