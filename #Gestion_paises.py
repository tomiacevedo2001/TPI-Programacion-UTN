#Gestion_paises
# Importamos la librería para manejar archivos CSV
import csv #Para leer y escribir archivos CSV
import os  #Para verificar si un archivo existe

# Obtiene la carpeta donde está guardado este archivo .py
CARPETA_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# Arma la ruta completa al CSV, siempre relativa a esa carpeta
ARCHIVO_CSV = os.path.join(CARPETA_SCRIPT, "paises.csv")

#Primero leemos y guardamos el archivo CSV
def leer_csv():
    #Lee el archivo y devuelve una lista de diccionarios
    #Cada diccionario es un pais
    #Si el archivo no existe, devuelve una lista vacia
    paises = []      #La lista vacia donde se guardan los paises

    #Verificamos si el archivo existe
    if not os.path.exists(ARCHIVO_CSV):
        print("Aviso. No se encontro el archivo. Se empieza con una lista vacia.")
        return paises
    
    #Abrimos el archivo en modo lectura
    with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)   # Lee fila → diccionario automáticamente

        numero_fila = 2   # Empezamos en 2 porque la fila 1 es el encabezado
        for fila in lector:
            pais = convertir_fila(fila, numero_fila)
            if pais is not None:            # Si la fila era válida, la agregamos
                paises.append(pais)
            numero_fila += 1
    
    print(f"Se cargaron {len(paises)} paises desde '{ARCHIVO_CSV}'.")
    return paises

def convertir_fila(fila, numero_fila):
    #Toma una fila del CSV (como diccionario de texto) y la convierte a un diccionario con los tipos correctos (int para números).
    #Devuelve None si algo está mal en esa fila.
    
    # Obtener cada campo y quitarle espacios en blanco
    nombre     = fila.get("nombre", "").strip()
    poblacion  = fila.get("poblacion", "").strip()
    superficie = fila.get("superficie", "").strip()
    continente = fila.get("continente", "").strip()

    # Verificar que ningún campo esté vacío
    if nombre == "" or poblacion == "" or superficie == "" or continente == "":
        print(f"  Advertencia - Fila {numero_fila}: tiene campos vacíos, se omite.")
        return None

    # Intentar convertir población y superficie a números enteros
    try:
        poblacion_numero  = int(poblacion)
        superficie_numero = int(superficie)
    except ValueError:
        print(f"  Advertencia - Fila {numero_fila}: población/superficie no son números, se omite.")
        return None

    # Verificar que los números sean positivos
    if poblacion_numero < 1 or superficie_numero < 1:
        print(f"  Advertencia - Fila {numero_fila}: valores deben ser mayores a 0, se omite.")
        return None

    # Si todo está bien, devolver el diccionario del país
    return {
        "nombre":     nombre,
        "poblacion":  poblacion_numero,
        "superficie": superficie_numero,
        "continente": continente
    }

def guardar_csv(paises):
    #Escribe la lista de paises en el archivo csv
    #Sobreecribe el archivo con los datos actuales
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        campos  = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()    # Escribe la primera fila con los nombres de columnas
        escritor.writerows(paises) # Escribe todos los países

#ENTRADA DE DATOS DEL USUARIO Y VALIDACIONES
def pedir_numero(mensaje, minimo=0):
    #Se le pide un numero entero al usuario. Sigue preguntadno hasta que se ingrese algo valido
    #El usuario puede escribir cancelar si lo desea, en este caso devuelve el numero puesto o none
    while True:
        entrada = input(mensaje).strip()
        #Si el usuario escribe cancelar
        if entrada.lower() == "cancelar":
            return None
        
        #Intentamos convertir a entero
        try:
            numero = int(entrada)
            if numero < minimo:
                print(f"El numero debe ser mayor o igual a {minimo}.")
            else:
                return numero #numero valido, se devuelve
        except ValueError:
            print("Ingrese un numero entero valido (o escriba 'cancelar').")

def pedir_texto(mensaje):
    #Le pedimos un texto al usuario y se repite hasta recibir algo que no este vacio
    #El usuario puede escribir "cancelar" si quiere salir. En este caso devuelve el texto o None
    while True:
        entrada = input(mensaje).strip()
        if entrada.lower() == "cancelar":
            return None
        if entrada != "":
            return entrada #Texto valido
        print("Este campo no puede estar vacio.")

def nombre_ya_existe(paises, nombre):
    #Revisa si ya existe un pais con ese nombre
    #La comparacion no distingue mayusculas
    #Devuelve True si existe, False si no
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False

#FUNCIONES DE OPERACIONES CON PAISES
def agregar_pais(paises):
    #Se le pide al usuario los datos de un nuevo pais y lo agrega a la lista
    #No se permieten nombres duplicados ni vacios
    print("AGREGAR PAIS (escriba cancelar para volver)")

    nombre = pedir_texto("Nombre del pais: ")
    if nombre is None:
        return #El usuario cancelo
    
    #Verificacmos si el nombre ya existe
    if nombre_ya_existe(paises, nombre):
        print(f"Error. El pais {nombre} ya esta en la lista.")
        return
    
    poblacion = pedir_numero("Poblacion: ", minimo=1)
    if poblacion is None:
        return
    
    superficie = pedir_numero("Superficie (km²): ", minimo=1)
    if superficie is None:
        return
    
    continente = pedir_texto("Continente: ")
    if continente is None:
        return
    
    #Creamos el diccionario del nuevo pais
    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    }

    #Y lo agregamos a la lista
    paises.append(nuevo_pais)
    print(f"Pais '{nombre}' agregado correctamente.")

def actualizar_pais(paises):
    #Busca un pais por su nombre y permite actualizar su poblacion y/o superficie
    print("ACTUALIZAR PAIS (escribe 'cancelar' para volver)")

    nombre = pedir_texto(" Nombre del pais a actualizar: ")
    if nombre is None:
        return
    
    #Buscar el pais en la lista
    pais_encontrado = None
    for pais in paises:
        if pais ["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break  #El pais fue encontrado, no hace falta seguir

    #Si no se encontro, se avisa y se sale
    if pais_encontrado is None:
        print(f"Error. No se encontro el pais '{nombre}'")
        return
    
    #Mostramos los datos actuales
    print(f"Pais: {pais_encontrado['nombre']}")
    print(f"Poblacion actual: {pais_encontrado['poblacion']:,}")
    print(f"Superficie actual: {pais_encontrado['superficie']:,} km²")
    print(f" (Deje en blanco y presione Enter para no modificar)")

    #Pedir nueva poblacion
    nueva_pob = input("Nueva poblacion (Enter para mantener): ").strip()
    if nueva_pob != "" and nueva_pob.lower() != "cancelar":
        try:
            valor = int(nueva_pob)
            if valor < 1:
                print("  Advertencia: valor inválido, no se actualizó la población.")
            else:
                pais_encontrado["poblacion"] = valor
        except ValueError:
            print("  Advertencia: no es un número, no se actualizó la población.")

    #Pedir nueva superficie
    nueva_sup = input("  Nueva superficie en km² (Enter para mantener): ").strip()
    if nueva_sup != "" and nueva_sup.lower() != "cancelar":
        try:
            valor = int(nueva_sup)
            if valor < 1:
                print("  Advertencia: valor inválido, no se actualizó la superficie.")
            else:
                pais_encontrado["superficie"] = valor
        except ValueError:
            print("  Advertencia: no es un número, no se actualizó la superficie.")
    
    print(f"\n  Datos de '{pais_encontrado['nombre']}' actualizados.")

#BUSQUEDA DE PAISES
def buscar_pais(paises):
    #Busca paises con lo que ingrese el usuario
    #No distingue mayusculas
    print("BUSCAR PAIS")

    termino = pedir_texto("Ingrese nombre o parte del nombre: ")
    if termino is None:
        return
    
    #Buscamos todos los paises que contengan el termino
    resultados = []
    for pais in paises:
        if termino.lower() in pais["nombre"].lower():
            resultados.append(pais)
    
    #Mostramos los resultados
    if len(resultados) == 0:
        print(f"No se encontraron paises que contengan '{termino}'.")
    else:
        print(f"Se encontraron {len(resultados)} resultado(s): ")
        mostrar_tabla(resultados)

#FILTROS
def filtrar_paises(paises):
    #hacemos el menu de filtros por continente, poblacion o superficie.
    print("FILTRAR PAISES")

    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")
    print("0. Volver")

    opcion = input("Opcion: ").strip()

    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")

def filtrar_por_continente(paises):
    #Muestra solo los paises del continente pedido
    continentes = []
    for pais in paises:
        if pais["continente"] not in continentes:
            continentes.append(pais["continente"])
    continentes.sort()

    print(f"\n  Continentes disponibles: {', '.join(continentes)}")

    continente = pedir_texto("Continente a filtrar: ")
    if continente is None:
        return
    
    #Filtramos
    resultados = []
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print(f" No hay paises en '{continente}'")
    else:
        print(f"Paises en {continente} ({len(resultados)}): ")
        mostrar_tabla(resultados)

def filtrar_por_poblacion(paises):
    #Muestra paises dentro del rango de poblacion establecido
    print("Ingrese el rango de poblacion: ")

    minimo = pedir_numero("Minimo: ", minimo=0)
    if minimo is None:
        return
    
    maximo = pedir_numero("Maximo: ", minimo=minimo)
    if maximo is None:
        return
    
    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"No hay paises con poblacion entre {minimo:,} y {maximo:,}.")
    else:
        print(f"Resultados ({len(resultados)}): ")
        mostrar_tabla(resultados)

def filtrar_por_superficie(paises):
    #Muestra países con superficie dentro del rango indicado.
    print("\n  Ingrese el rango de superficie (km²):")

    minimo = pedir_numero("  Mínimo (km²): ", minimo=0)
    if minimo is None:
        return

    maximo = pedir_numero("  Máximo (km²): ", minimo=minimo)
    if maximo is None:
        return

    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print(f"\n  No hay países con superficie entre {minimo:,} y {maximo:,} km².")
    else:
        print(f"\n  Resultados ({len(resultados)}):\n")
        mostrar_tabla(resultados)

#ORDENAMIENTO
def ordenar_paises(paises):
    #Ordena y muestra los paises segun el criterio elegido
    #Usa la funcion sorted()
    print("ORDENAR PAISES")

    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")
    print("0. Volver")

    opcion = input("Criterio: ").strip()
    if opcion == "0":
        return
    
    #Hacemos las opciones
    if opcion == "1":
        clave = "nombre"
    elif opcion == "2":
        clave = "poblacion"
    elif opcion == "3":
        clave = "superficie"
    else:
        print("Opcion invalida")
        return
    
    print("Direccion: ")
    print("1. Ascendente (menor a mayor)")
    print("2. Descendente (mayor a menor)")
    direccion = input("Opcion: ").strip()

    if direccion == "1":
        de_mayor_a_menor = False
    elif direccion == "2":
        de_mayor_a_menor = True
    else:
        print("Opcion invalida")
        return

    def obtener_nombre(pais):
        return pais["nombre"]

    def obtener_poblacion(pais):
        return pais["poblacion"]

    def obtener_superficie(pais):
        return pais["superficie"]

    # Y luego según lo que eligió el usuario:
    if clave == "nombre":
        ordenados = sorted(paises, key=obtener_nombre, reverse=de_mayor_a_menor)
    elif clave == "poblacion":
        ordenados = sorted(paises, key=obtener_poblacion, reverse=de_mayor_a_menor)
    elif clave == "superficie":
        ordenados = sorted(paises, key=obtener_superficie, reverse=de_mayor_a_menor)
    
    etiqueta = "descendente" if de_mayor_a_menor else "ascendente"
    
    print(f"Ordenado por {clave} ({etiqueta}): ")
    mostrar_tabla(ordenados)    
    
#ESTADISTICAS
def mostrar_estadisticas(paises):
    #Calcula y muestra:
    #Pais con mayor y menor poblacion
    #Promedio de poblacion y superficie
    #Cantidad de paises por continente
    print("ESTADISTICAS")

    def buscar_mayor_poblacion(paises):
        mayor = paises[0]           # empezamos asumiendo que el primero es el mayor
        for pais in paises:
            if pais["poblacion"] > mayor["poblacion"]:
                mayor = pais        # encontramos uno más grande, actualizamos
        return mayor

    def buscar_menor_poblacion(paises):
        menor = paises[0]
        for pais in paises:
            if pais["poblacion"] < menor["poblacion"]:
                menor = pais
        return menor

# Lo mismo para superficie:
    def buscar_mayor_superficie(paises):
        mayor = paises[0]
        for pais in paises:
            if pais["superficie"] > mayor["superficie"]:
                mayor = pais
        return mayor

    def buscar_menor_superficie(paises):
        menor = paises[0]
        for pais in paises:
            if pais["superficie"] < menor["superficie"]:
                menor = pais
        return menor
    
    mayor_pob = buscar_mayor_poblacion(paises)
    menor_pob = buscar_menor_poblacion(paises)
    mayor_sup = buscar_mayor_superficie(paises)
    menor_sup = buscar_menor_superficie(paises)
    
    # Promedios
    suma_poblacion = 0
    for pais in paises:
        suma_poblacion += pais["poblacion"]
        promedio_poblacion = suma_poblacion / len(paises)

    suma_superficie = 0
    for pais in paises:
        suma_superficie += pais["superficie"]
        promedio_superficie = suma_superficie / len(paises)

    # Contar por continente
    contador = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in contador:
            contador[continente] += 1
        else:
            contador[continente] = 1

    # Mostrar todo
    print(f"\nTotal de paises: {len(paises)}")
    print(f"\n--- POBLACION ---")
    print(f"Mayor: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab.)")
    print(f"Menor: {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab.)")
    print(f"Promedio: {promedio_poblacion:,.0f} hab.")
    print(f"\n--- SUPERFICIE ---")
    print(f"Mayor: {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"Menor: {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"Promedio: {promedio_superficie:,.0f} km²")
    print(f"\n--- POR CONTINENTE ---")
    for continente in sorted(contador):
        print(f"  {continente:<15} {contador[continente]:>3}  {'#' * contador[continente]}")

#MOSTRAR TABLA
def mostrar_tabla(paises):
    #Imprime los países en forma de tabla con columnas alineadas.
    #El formato :, en los números agrega separadores de miles (1,000,000).
    #El formato :< alinea a la izquierda, :> alinea a la derecha.

    if len(paises) == 0:
        print("  (Lista vacía)")
        return

    #Encabezado de la tabla
    print(f"  {'N°':<4} {'NOMBRE':<25} {'POBLACIÓN':>14} {'SUPERFICIE':>13} {'CONTINENTE'}")
    print(f"  {'─'*4} {'─'*25} {'─'*14} {'─'*13} {'─'*15}")

    #Una fila por país
    numero = 1
    for pais in paises:
        print(
            f"  {numero:<4} "
            f"{pais['nombre']:<25} "
            f"{pais['poblacion']:>14,} "
            f"{pais['superficie']:>10,} km²  "
            f"{pais['continente']}"
        )
        numero += 1
    print()

def listar_todos(paises):
    #Muestra todos los países en la lista.
    print(f"  LISTA COMPLETA ({len(paises)} países)")

    if len(paises) == 0:
        print("  No hay países registrados.")
    else:
        mostrar_tabla(paises)

#MENU PRINCIPAL
def mostrar_menu():
    #Imprime las opciones disponibles.
    print("   SISTEMA DE GESTIÓN DE PAÍSES")
    print("  1. Listar todos los países")
    print("  2. Agregar un país")
    print("  3. Actualizar población / superficie")
    print("  4. Buscar país por nombre")
    print("  5. Filtrar países")
    print("  6. Ordenar países")
    print("  7. Estadísticas")
    print("  0. Guardar y salir")

def main():
    #Punto de entrada del programa.
    #1. Carga los países desde el CSV.
    #2. Muestra el menú en un bucle infinito.
    #3. Ejecuta la opción elegida.
    #4. Al elegir 0, guarda y termina.
    print("Iniciando Sistema de Gestión de Países...")

    #Cargar datos al arrancar
    paises = leer_csv()

    #Bucle principal: se repite hasta que el usuario elija salir
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_todos(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            guardar_csv(paises)
            print("Datos guardados.")
            break   # Sale del while True
        else:
            print("Opción inválida. Ingrese un número del 0 al 7.")

#Arranque del programa
#Esto hace que main() sólo se llame cuando ejecutamos
#este archivo directamente (no cuando lo importamos).
if __name__ == "__main__":
    main()

