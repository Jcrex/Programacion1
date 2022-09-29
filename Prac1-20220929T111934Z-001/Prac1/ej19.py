cad1, cad2 = input("introduce una cadena: "), input("introduce un separador: ")
num = int(input("introduce un número entero: "))
print("{0}{1}".format(cad1,cad2)*(num-1) + cad1 )