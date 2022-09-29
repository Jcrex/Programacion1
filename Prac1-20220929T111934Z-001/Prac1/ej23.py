import math as ma
num1, num2, rad = (int(input("introduce el primer lado: ")), int(input("introduce el segundo lado: ")),
                   float(input("introduce el ángulo (en radianes): ")))
print("el área del triángulo es: ", ((num1 * num2)/2)*ma.sin((ma.radians(rad))))
#print("el area es (sin usar la funcion radians()) ", ((num1 * num2)/2)*(rad * ma.pi/180))
