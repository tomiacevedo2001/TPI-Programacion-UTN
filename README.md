# Sistema de Gestión de Países

Aplicación de consola desarrollada en **Python 3** para gestionar información sobre países. Permite cargar, consultar, filtrar, ordenar y obtener estadísticas de un dataset de países almacenado en un archivo CSV.

---

## Descripción

El sistema permite:

- **Listar** todos los países registrados en formato tabla.
- **Agregar** nuevos países con validación de datos.
- **Actualizar** la población y superficie de un país existente.
- **Buscar** países por nombre (coincidencia parcial o exacta).
- **Filtrar** por continente, rango de población o rango de superficie.
- **Ordenar** por nombre, población o superficie (ascendente/descendente).
- **Ver estadísticas**: mayor/menor población y superficie, promedios, cantidad por continente.

---

## Estructura del Proyecto

```
paises_app/
├── main.py        # Código fuente principal
├── paises.csv     # Dataset base con 32 países
└── README.md      # Este archivo
```

---

## Instrucciones de Uso

### Requisitos

- Python 3.10 o superior
- No se requieren librerías externas (solo módulos estándar: `csv`, `os`).

### Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/usuario/paises_app.git
cd paises_app

# Ejecutar el programa
python main.py
```

### Menú principal

```
══════════════════════════════════════════════════════════════
   SISTEMA DE GESTIÓN DE PAÍSES
══════════════════════════════════════════════════════════════
  1. Listar todos los países
  2. Agregar un país
  3. Actualizar población / superficie
  4. Buscar país por nombre
  5. Filtrar países
  6. Ordenar países
  7. Estadísticas
  0. Guardar y salir
══════════════════════════════════════════════════════════════
```

---

## Ejemplos de Entradas y Salidas

###  Agregar un país

```
  AGREGAR PAÍS  (escriba 'cancelar' para volver)
  ────────────────────────────────────────────────────────────
  Nombre del país: Cuba
  Población: 11256372
  Superficie (km²): 109884
  Continente: América

  ✔  País 'Cuba' agregado correctamente.
```

### Buscar por nombre

```
  Ingrese nombre o parte del nombre: ar

  Se encontraron 2 resultado(s):

  #    NOMBRE                       POBLACIÓN   SUPERFICIE CONTINENTE
  ──── ──────────────────────────── ────────── ─────────── ──────────────────
  1    Argentina                   45.376.763  2.780.400 km² América
  2    Arabia Saudita              35.013.414  2.149.690 km² Asia
```

### Filtrar por continente

```
  Continentes disponibles: África, América, Asia, Europa, Oceanía
  Continente a filtrar: Oceanía

  Países en Oceanía (2):

  #    NOMBRE                       POBLACIÓN   SUPERFICIE CONTINENTE
  ──── ──────────────────────────── ────────── ─────────── ──────────────────
  1    Australia                   25.921.100  7.692.024 km² Oceanía
  2    Nueva Zelanda                5.122.600    268.021 km² Oceanía
```

### Estadísticas

```
  Total de países registrados: 32

  ─────────────────────────────────────────
  POBLACIÓN
  ─────────────────────────────────────────
  Mayor población : China                    1.412.600.000 hab.
  Menor población : Uruguay                      3.530.912 hab.
  Promedio        :                            125.430.221 hab.

  PAÍSES POR CONTINENTE
  ─────────────────────────────────────────
  África          5   █████
  América        10   ██████████
  Asia            8   ████████
  Europa          7   ███████
  Oceanía         2   ██
```

### Manejo de errores

```
  Nombre del país: Argentina
  El país 'Argentina' ya existe.

  Población: abc
  Por favor ingrese un número entero válido (o 'cancelar').
```

---

## Formato del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

- `nombre`: texto, no vacío.
- `poblacion`: entero positivo.
- `superficie`: entero positivo (km²).
- `continente`: texto, no vacío.

Las filas con campos vacíos o valores no numéricos en `poblacion`/`superficie` son ignoradas con advertencia.

---

## Integrantes del Equipo

| Integrantes |
|---|---|
| Tomas Ignacio Acevedo Peña | 
| Gabriel Alfredo Brizuela Jimenez  | 

---

## Materia

**Programación 1** — Trabajo Práctico Integrador 
Lenguaje: Python 3 · Estructuras: listas, diccionarios, funciones, CSV
