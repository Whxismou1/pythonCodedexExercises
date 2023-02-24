height = int(input("Introduce tu altura en cm: ")) 
credits = int(input("Introduce tus creditos: ")) 
with_taller_person = False

if height >= 137 and credits >= 10:
    print("Enjoy the ride :)")
elif height < 200:
    if height < 100 or (not with_taller_person):
        print("You´re not tall enough for this ride yet")
    elif height >= 100 and with_taller_person:
        print("Enjoy the ride!")
if credits < 10:
    print("You dont have enough credits to ride")