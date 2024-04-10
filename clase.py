import os

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para imprimir el encabezado
def imprimir_encabezado():
    print("Evaluación N°1 Redes Avanzadas I")
    print("Integrantes:")
    print("- Nombre1 Apellido1")
    print("- Nombre2 Apellido2")
    print("- Nombre3 Apellido3")
    # Puedes agregar más nombres si es necesario
    print()

# Función para solicitar información al usuario
def solicitar_informacion():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    codigo_seccion = input("Ingrese su Código-sección: ")
    sede = input("Ingrese su sede: ")
    return nombre, apellido, codigo_seccion, sede

# Función para mostrar la información ingresada por el usuario
def mostrar_informacion(nombre, apellido, codigo_seccion, sede):
    limpiar_pantalla()
    print("Información ingresada:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Código-sección:", codigo_seccion)
    print("Sede:", sede)
    print()

# Función para determinar el tipo de ACL IPv4
def determinar_tipo_acl(numero_acl):
    if numero_acl.isdigit():
        numero_acl = int(numero_acl)
        if 1 <= numero_acl <= 99:
            print("Es una ACL Estándar.")
        elif 100 <= numero_acl <= 199:
            print("Es una ACL Extendida.")
        else:
            print("El número no corresponde a una lista de acceso.")
    else:
        print("Por favor, ingrese un número válido.")

# Función principal
def main():
    limpiar_pantalla()
    imprimir_encabezado()
    nombre, apellido, codigo_seccion, sede = solicitar_informacion()
    mostrar_informacion(nombre, apellido, codigo_seccion, sede)
    numero_acl = input("Ingrese el número de ACL IPv4: ")
    determinar_tipo_acl(numero_acl)

if __name__ == "__main__":
    main()
