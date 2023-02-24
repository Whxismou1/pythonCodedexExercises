yuans = int(input("How many yuans have you got: "))
yens = int(input("How many yens have you got: "))
wons = int(input("How many wons have you got: "))

dolarYuan = yuans * 0.14561418
dolarYen = yens * 0.0074543395
dolarWon = wons * 0.00077168549

dolarsTot = dolarYuan + dolarYen + dolarWon

print("Total en dolares es: $", dolarsTot)