# 🎮 Cuatro en Línea – Python (Consola)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Library-pandas-green?logo=pandas)
![Console](https://img.shields.io/badge/Mode-Consola-lightgrey)
![Status](https://img.shields.io/badge/Proyecto-Académico-orange)

---

## 📌 Descripción

Este repositorio contiene una versión en consola del clásico juego **Cuatro en Línea (Connect Four)**.  
Fue desarrollado como **proyecto académico en 2022** en la Universidad Nacional de Colombia, pero llevado un paso más allá para fortalecer habilidades de programación.  

Incluye no solo los fundamentos de programación en Python, sino también características más avanzadas como:

- ✅ **Validaciones robustas** de entrada numérica y de cadenas.  
- ✅ **Control completo del flujo de juego**: turnos, reinicios, detección de empate.  
- ✅ **Gestión de puntajes** con `pandas.DataFrame`, permitiendo llevar estadísticas de jugadores.  
- ✅ Uso de la librería estándar `random` para generar variaciones en el juego.  

📚 **Autor:** Juan Pablo Marín Montoya  

---

## 🗂️ Organización del repositorio
El proyecto está organizado en un único script de Python que gestiona:

- 📋 **Menú principal** con opciones de juego, puntajes y salida.  
- 🎲 **Lógica del juego** con tablero dinámico en consola.  
- 🏆 **Scoreboard** con registro de victorias y derrotas.  

---

## 🏆 Ejemplo de scoreboard
Después de varias partidas, las estadísticas de jugadores se almacenan en un **DataFrame**:  

```python
    Jugador   Ganadas  Perdidas
0  Juan       2        1
1  María      1        2
