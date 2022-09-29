import math as ma
num1, num2, num3 = (int(input("Introduce a: ")), int(input("Introduce b: ")),
                    int(input("Introduce c: ")))
print("X1 = ", ((-num2) + (ma.sqrt((num2**2)-(4*num1*num3)))) / (2 * num1))
print("X2 = ", ((-num2) - (ma.sqrt((num2**2)-(4*num1*num3)))) / (2 * num1))