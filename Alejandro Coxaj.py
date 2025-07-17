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
    print("Opción no válida. ")