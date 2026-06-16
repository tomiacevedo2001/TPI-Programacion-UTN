# Sistema de Gestión de Países

Aplicación de consola desarrollada en Python que permite administrar
información sobre países (nombre, población, superficie y continente)
almacenada en un archivo CSV.

Trabajo Práctico — Programación 1

## Integrantes

- Tomas Ignacio Acevedo Peña
- Gabriel Alfredo Brizuela Jimenez

Año: 2026

---

## Descripción general

El programa carga los datos desde un archivo `paises.csv` al iniciar,
los mantiene en memoria como una **lista de diccionarios** durante la
ejecución, y los vuelve a guardar en el mismo archivo al salir.

Cada país se representa con la siguiente estructura:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}
```

---

## Requisitos

- Python 3.x (no requiere librerías externas, solo módulos estándar:
  `csv` y `os`)

---

## Cómo ejecutar el programa

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tomiacevedo2001/TPI-Programacion-UTN.git
   ```
2. Entrar a la carpeta del proyecto:
   ```bash
   cd TPI-Programacion-UTN
   ```
3. Ejecutar el programa:
   ```bash
   python gestion_paises.py
   ```

El archivo `paises.csv` debe estar en la **misma carpeta** que el
script. El programa busca el archivo de forma automática usando la
ubicación del propio script, por lo que funciona sin importar desde
qué directorio se lo ejecute.

---

## Formato del archivo CSV

El archivo `paises.csv` debe tener el siguiente encabezado y formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

| Campo | Tipo | Descripción |
|-------|------|-------------|
| nombre | texto | Nombre del país |
| poblacion | número entero | Cantidad de habitantes |
| superficie | número entero | Superficie en km² |
| continente | texto | Continente al que pertenece |

Si una fila del CSV tiene campos vacíos, valores no numéricos o
números negativos, esa fila se descarda automáticamente y el programa
muestra una advertencia indicando el número de línea afectado.

---

## Menú principal

Al ejecutar el programa se muestra el siguiente menú:

```
   SISTEMA DE GESTIÓN DE PAÍSES
  1. Listar todos los países
  2. Agregar un país
  3. Actualizar población / superficie
  4. Buscar país por nombre
  5. Filtrar países
  6. Ordenar países
  7. Estadísticas
  0. Guardar y salir
```

---

## Funcionalidades

### 1. Listar todos los países

Muestra una tabla con todos los países cargados, con columnas
alineadas para nombre, población, superficie y continente.

### 2. Agregar un país

Solicita nombre, población, superficie y continente. No permite:

- Campos vacíos
- Países con un nombre que ya existe (sin distinguir mayúsculas)
- Valores de población o superficie menores a 1

En cualquier momento se puede escribir `cancelar` para volver al menú
sin guardar cambios.

**Ejemplo de uso:**
```
AGREGAR PAIS (escriba cancelar para volver)
Nombre del pais: México
Poblacion: 128900000
Superficie (km²): 1964375
Continente: América

Pais 'México' agregado correctamente.
```

### 3. Actualizar población / superficie

Busca un país por nombre (coincidencia exacta, sin distinguir
mayúsculas) y permite modificar su población y/o superficie. Si se
presiona Enter sin escribir nada, el valor original no se modifica.

**Ejemplo de uso:**
```
ACTUALIZAR PAIS (escribe 'cancelar' para volver)
 Nombre del pais a actualizar: argentina
Pais: Argentina
Poblacion actual: 45,376,763
Superficie actual: 2,780,400 km²
 (Deje en blanco y presione Enter para no modificar)
Nueva poblacion (Enter para mantener): 46000000
  Nueva superficie en km² (Enter para mantener):

  Datos de 'Argentina' actualizados.
```

### 4. Buscar país por nombre

Permite buscar por coincidencia **parcial**, sin distinguir entre
mayúsculas y minúsculas.

**Ejemplo de uso:**
```
BUSCAR PAIS
Ingrese nombre o parte del nombre: arg
Se encontraron 1 resultado(s):
  N°   NOMBRE                       POBLACIÓN    SUPERFICIE CONTINENTE
  1    Argentina                   45,376,763   2,780,400 km²  América
```

### 5. Filtrar países

Ofrece tres tipos de filtro:

- **Por continente:** muestra los continentes disponibles y filtra
  los países que pertenecen al continente ingresado.
- **Por rango de población:** solicita un valor mínimo y máximo, y
  muestra los países cuya población está dentro de ese rango.
- **Por rango de superficie:** igual que el anterior, pero
  comparando la superficie en km².

Si ningún país cumple la condición, se muestra un mensaje indicando
que no hay resultados.

### 6. Ordenar países

Permite ordenar la lista completa según tres criterios:

- Nombre (orden alfabético)
- Población
- Superficie

Y en dos direcciones:

- Ascendente (menor a mayor)
- Descendente (mayor a menor)

El ordenamiento se realiza con la función `sorted()` de Python,
utilizando funciones auxiliares (`obtener_nombre`, `obtener_poblacion`,
`obtener_superficie`) como criterio de comparación.

### 7. Estadísticas

Calcula y muestra:

- País con mayor y menor población
- País con mayor y menor superficie
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente, con una barra visual simple

Si no hay países cargados, se muestra un mensaje indicando que no hay
datos suficientes para calcular estadísticas.

**Ejemplo de salida:**
```
ESTADISTICAS

Total de paises: 4

--- POBLACION ---
Mayor: Brasil (213,993,437 hab.)
Menor: Alemania (83,149,300 hab.)
Promedio: 117,079,875 hab.

--- SUPERFICIE ---
Mayor: Brasil (8,515,767 km²)
Menor: Alemania (357,022 km²)
Promedio: 3,007,786 km²

--- POR CONTINENTE ---
  América          2  ##
  Asia             1  #
  Europa           1  #
```

### 0. Guardar y salir

Escribe todos los cambios (altas y modificaciones) en `paises.csv`,
sobrescribiendo el archivo, y finaliza el programa.

---

## Validaciones implementadas

- Lectura del CSV: se descartan filas con campos vacíos, valores no
  numéricos o valores negativos, mostrando una advertencia con el
  número de línea.
- Entradas numéricas: se valida que sean enteros y, cuando
  corresponde, mayores o iguales a un mínimo (por ejemplo, población
  y superficie deben ser mayores a 0).
- Entradas de texto: no se permiten campos vacíos.
- Nombres duplicados: no se puede agregar un país que ya existe
  (comparación sin distinguir mayúsculas).
- Cancelación: en los formularios de alta y modificación, el usuario
  puede escribir `cancelar` en cualquier momento para volver al menú
  sin aplicar cambios.
- Búsquedas y filtros sin resultados: se informa al usuario en lugar
  de mostrar una tabla vacía o producir un error.
- Estadísticas sobre lista vacía: se valida antes de calcular para
  evitar errores si no hay países cargados.

---

## Estructura del repositorio

```
TPI-Programacion-UTN/
├── #Gestion_paises.py    Programa principal
├── paises.csv            Dataset de países
└── README.md             Este archivo
```

---

## Conceptos de Programación 1 aplicados

| Concepto | Ejemplo en el código |
|----------|----------------------|
| Listas | `paises = []`, `paises.append(...)` |
| Diccionarios | Cada país representado como `{"nombre": ..., "poblacion": ..., ...}` |
| Funciones | Una función por responsabilidad (`leer_csv`, `agregar_pais`, `ordenar_paises`, etc.) |
| Condicionales | `if` / `elif` / `else` para el menú y las validaciones |
| Bucles | `while True` para el menú y las validaciones de entrada; `for` para recorrer la lista de países |
| Manejo de archivos | `csv.DictReader` y `csv.DictWriter` para leer y escribir `paises.csv` |
| Manejo de errores | `try` / `except ValueError` al convertir texto a números |
| Ordenamiento | `sorted()` con funciones auxiliares como criterio (`key`) |
| Estadísticas básicas | Cálculo de máximos, mínimos, promedios y conteos por categoría |

---

## Enlaces

- Video demostrativo: https://drive.google.com/file/d/1ji6AS46nbAGnb2BWGq6NsiXTKqPMQnh5/view?usp=sharing
- Link Repositorio en GitHub: https://github.com/tomiacevedo2001/TPI-Programacion-UTN
- Link Archivo PDF: https://drive.google.com/file/d/1tZOdbIk_8fTOKOzIrZHV7DSmxxg3DiZ3/view?usp=sharing
