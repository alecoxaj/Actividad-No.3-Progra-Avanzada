print("Bienvenido a la Calculadora 3000 ")
a = float(input("Ingrese el primer número: "))

b = float(input("Ingrese el segundo número: "))

print("\nSeleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese una opción (1/2/3/4): ")

if opcion == "1":
    print("Resultado de la suma:", a + b)
elif opcion == "2":
    print("Resultado de la resta:", a - b)
elif opcion == "3":
    print("Resultado de la multiplicación:", a * b)
elif opcion == "4":
    if b != 0:
        print("Resultado de la división:", a / b)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida.")

