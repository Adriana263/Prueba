while True:
    print("1. Suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    opcion = int(input("Que operacion quieres hacer: "))
    n1 = float(input("ingresa un numero: ")) 
    n2 = float(input("ingresa un numero: "))
    if opcion == 1:
        result = n1 + n2
        print(f"{n1} + {n2} = {result}")
    elif opcion == 2:
        result = n1 - n2
        print(f"{n1} - {n2} = {result}")
    elif opcion == 3:
        result = n1 * n2
        print(f"{n1} * {n2} = {result}")
    elif opcion == 4:
        result = n1 / n2 
        print(f"{n1} / {n2} = {result}")
    else:
        print("Opcion ingresada incorrecta")
    print("Si")
    print("No")
    Seguir = str(input("Desea continuar: "))
    if Seguir == "si":
        continue
    elif Seguir == "no":
        break
    else:
        break
