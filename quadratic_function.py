print("************************************")
print("Bienvenido a la calculadora de ecuaciones de 2º grado")
print("ax² + bx + c = 0")
print("************************************")
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))
print("************************************")
root1 = ((b*-1) + ((b**2) - (4*a*c))**0.5) / (2 * a)
root2 = ((b*-1) - ((b**2) - (4*a*c))**0.5) / (2 * a)
print("La x positiva da: ", root1)
print("La x negativa da: ", root2)