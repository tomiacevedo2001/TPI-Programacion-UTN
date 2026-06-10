#Gestion_paises



# Importamos la librería para manejar archivos CSV
import csv

# Lista de paises por defecto (Plan B)
lista_paises = [
    ["Argentina", 45376763, 2780400, "América"],
    ["Venezuela", 28838499, 916445, "América"],
    ["Japón", 125124000, 377975, "Asia"],
    ["Nueva Zelanda", 5124100, 268021, "Oceanía"],
    ["España", 47420000, 505990, "Europa"],
    ["Egipto", 110990000, 1001450, "África"]
    ]

# Leemos el archivo
try:
    archivo = open("paises.csv", "r")
    lista_paises = []
    
    for linea in archivo:
        # Si la línea tiene los títulos de las columnas, la saltamos y seguimos con la siguiente
        if "poblacion" in linea.lower() or "nombre" in linea.lower():
            continue
            
        datos = linea.strip().split(",")
        
        # Armamos la sublista con tus tipos de datos
        pais_nuevo = [datos[0], int(datos[1]), int(datos[2]), datos[3]]
        lista_paises.append(pais_nuevo)

    # Cerramos el archivo     
    archivo.close()
    print("Datos cargados correctamente.")

except FileNotFoundError:
    print("Usando lista por defecto.")


def mostrar_menu():
    print("\n==== SISTEMA DE GESTIÓN DE PAÍSES ===")
    print("1. Agregar un país")
    print("2. Actualizar Población y Superficie")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

# ESTE ES EL FLUJO PRINCIPAL
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")

 # ======================================================================================================   
    # Agregar_pais()
    
    if opcion == "1":
        print(">> Elegiste agregar pais <<")
        
        volver_al_menu = False
        # Validamos el pais con bucle <<<
        while True:
            # Eliminamos espacios al comienzo y final del texto
            pais = input("Ingrese el pais o coloque 7 para volver al menu principal: ").strip()

            if pais == "7":
                volver_al_menu = True
                break

        # Eliminamos espacios entre el texto para validarlo despues con isalpha
            solo_letras = pais.replace(" ", "") 

            if pais == "": # >> Si el usuario ingresa solo espacio arrojamos error
                print("Error el nombre no puede estar vacio")
 

        # Validamos si es un string y no un numero o cualquier otro dato 
            elif not solo_letras.isalpha():
                print("Error debe contener solo letras no datos numericos")  

        # En caso contrario paramos y seguimos con los otros datos          
            else:
                break 
        if volver_al_menu == False:   
            

        # Validamos poblacion con bucle <<<  

            while True: 
            # En caso que pueda fallar, # usaremos (try/except) para evaluar errores sin que falle el programa
                try:
                    poblacion = int(input("Ingrese la poblacion: ")) # << Convertimos directamente a numero entero

            # Condicionamos Si es menor a 0 solicitamos de nuevo el numero
                    if poblacion <=0:
                        print("Error la poblacion debe ser mayor que cero")

            # En caso de ingresar bien los datos, paramos aca el bucle y seguimos      
                    else:
                        break 
            # Si el usuario ingresa cualquier otro dato no numerico arrojamos el error     
                except ValueError:
                    print("Debe ingresar un numero entero sin letras ni puntos")        
     
        # Validamos superficie con el bucle <<<<<<< 
            while True:

           # Usamos (try/except) para evitar que falle el programa en caso de un dato erroneo 
                try:
                    superficie = int(input("Ingrese la superficie en km2: "))

            # Condiconamos si los datos no son correctos     
                    if superficie <= 0:
                        print("Error la superficie no puede ser menor a 0 ")

                    else: # Paramos si el usuario igresa correctamente los datos
                        break
                except ValueError: # >> En caso de ingresar un dato no numerico 
                    print("Debe ingresar un numero valido")

        # Validamos continente <<<<<<<
            while True:
                continente = input("Ingrese el continente: ").strip()

            # Eliminamos espacios entre el texto para validar la cadena str luego
                sin_numeros = continente.replace(" ", "") 

                if continente == "": # >>> Validamos que no haya un espacio vacio 
                    print("Error no puede quedar el campo vacio")

        # Validamos si es un str y no cualquier otro dato    
                elif not sin_numeros.isalpha(): #>>> Validamos que sea un str
                    print("Error ingrese un dato valido") 

        # Si el dato que esperamos es correcto, paramos el bucle
                else:
                    break
      
    # Guardamos cada una de las variables en una lista que llevara el nombre de nuevo pais  
            nuevo_pais = [pais, poblacion, superficie, continente]
    
    # Esa lista la guardamos dentro de la lista de paises y quedara actualizada 
            lista_paises.append(nuevo_pais)

    # Procedemos a dar un aviso para que el usuario sepa que los datos han sido guardados correctamente
            print(f"\n{pais} Guardado con exito")        
     

    # =============================================================================================== 
     
    # Actualizar poblacion y superficie () 
    elif opcion == "2":
        print(">>> Elegiste actualizar datos <<<")

        encontrado = False
        
        while encontrado == False:
         # Solicitamos el pais del que vamos actualizar sus datos y eliminamos espacios       
            buscar_pais = input("Ingrese que pais quiere actualizar o coloque 7 para volver: ").strip()

            if buscar_pais == "7":
                break
    
        # Recorremos la lista para encontrar el pais
            for pais in lista_paises:

            # Comparamos si esta el nombre en las listas anidadas
                if pais[0].replace(" ", "").lower() == buscar_pais.replace(" ","").lower(): 
                    try:
                    # Solicitamos la nueva poblacion y superficie
                        nueva_pob = int(input("Ingrese datos de la nueva poblacion: "))
                        nueva_sup = int(input("Ingrese datos de nueva superficie: "))

                        pais[1] = nueva_pob # Guardamos la nueva poblacion en la lista pais
                        pais[2] = nueva_sup # Guardamos la nueva superficie en la lista pais

                        print("La poblacion y superficie de ha sido actualizada correctamente")

                        encontrado = True
                        break

                    except ValueError:
                        print("Error debes ingresar numeros validos")
                        break

            if encontrado == False:
                print("El pais no se encuentra en la lista")

    # =====================================================================================================            


    elif opcion == "3":
        print("-> Elegiste: Buscar país")

        encontrado = False

        # El bucle se repetirá mientas 'encontrado' sea False
        while encontrado == False:
            # 1. Pedimos el país y limpiamos espacios de los bordes
            nombre_buscar = input("Ingrese el pais a buscar: ").strip()

            # 2. Recorremos la lista de países 
            for pais in lista_paises:
        
                # 3. Comparamos limpiando espacios en ambos lados para evitar fallos
                if pais[0].replace(" ", "").lower() == nombre_buscar.replace(" ", "").lower():
                    print("\n===============================")
                    print(f"País encontrado: {pais[0]}")
                    print(f"Población: {pais[1]} habitantes")
                    print(f"Superficie: {pais[2]} km²")
                    print(f"Continente: {pais[3]}")
                    print("===============================")
            
                    encontrado = True
                    break  # Detiene el bucle for. Al salir, el 'while' verá que 'encontrado' es True y también terminará.

            # 4. Si terminó el for y no lo encontramos, avisamos y el while vuelve a empezar
            if encontrado == False:
                print(" El país no se encuentra registrado. Intente nuevamente.\n")

    # =====================================================================================================    
    elif opcion == "4":
        print("-> Elegiste: Filtrar")



    elif opcion == "5":
        print("-> Elegiste: Ordenar")
    elif opcion == "6":
        print("-> Elegiste: Estadísticas")
    elif opcion == "7":
        print("¡Gracias por usar el sistema! Saliendo...")
        break # Rompe el bucle y cierra el programa
    else:
        print("Error: Opción inválida. Intente de nuevo.")
