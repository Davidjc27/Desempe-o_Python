carritos = {}

def agregar_carro():
    nombre = input("Ingrese el nombre del carro: ")
    marca = input("Ingrese la marca del carro: ")
    color = input("Ingrese el color del carro: ")
    carritos[nombre] = {"Marca": marca, "Color": color}
    print(f"El carro {nombre} se ha agregado al diccionario.")

def buscar_carro():
    nombre = input("Ingrese el nombre del carro que desea buscar: ")
    carro = carritos.get(nombre)
    if carro:
        print(f"Información del carro {nombre}:")
        print(f"Marca: {carro['Marca']}")
        print(f"Color: {carro['Color']}")
    else:
        print(f"El carro {nombre} no se encuentra en el diccionario.")

def actualizar_carro():
    nombre = input("Ingrese el nombre del carro que desea actualizar: ")
    carro = carritos.get(nombre)
    if carro:
        marca = input("Ingrese la nueva marca del carro: ")
        color = input("Ingrese el nuevo color del carro: ")
        carro['Marca'] = marca
        carro['Color'] = color
        print(f"La información del carro {nombre} se ha actualizado.")
    else:
        print(f"El carro {nombre} no se encuentra en el diccionario.")

def eliminar_carro():
    nombre = input("Ingrese el nombre del carro que desea eliminar: ")
    if nombre in carritos:
        del carritos[nombre]
        print(f"El carro {nombre} se ha eliminado del diccionario.")
    else:
        print(f"El carro {nombre} no se encuentra en el diccionario.")

while True:
    print("\nMenu:")
    print("1. Agregar")
    print("2. Buscar")
    print("3. Actualizar dato")
    print("4. Eliminar elemento")
    print("5. Salir")
    
    opcion = input("Digite la opción: ")
    
    if opcion == "1":
        agregar_carro()
    elif opcion == "2":
        buscar_carro()
    elif opcion == "3":
        actualizar_carro()
    elif opcion == "4":
        eliminar_carro()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
