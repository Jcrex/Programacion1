import math as ma
num1, num2 = int(input("Introduce el primer lado: ")), int(input("Introduce el segundo lado: "))
rad = float(input("Introduce el ángulo (en radianes): "))
print("El área del triángulo es: ", round(((num1 * num2)/2)*ma.sin(rad), 2))
