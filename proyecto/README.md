# 📈 Analizador de PIB - Comparativa OCDE

Este proyecto nace de la necesidad de explorar datos económicos reales de forma visual e interactiva, evitando las planillas de datos aburridas y transformándolas en un dashboard accesible para cualquiera.

👉 [https://miproyectofinalpib.streamlit.app/](https://miproyectofinalpib.streamlit.app/)

---

## ¿Qué hace esta app?

1. **Gráfica tendencias:** Muestra en un solo gráfico la curva histórica del país seleccionado frente a la tendencia general de la OCDE.
2. **Cálculos en vivo:** Al deslizar la barra de años, calcula automáticamente:
   * El PIB del país en ese año específico.
   * El PIB promedio general.
   * La brecha/diferencia entre ambos valores (redondeada a un decimal).
3. **Interfaz amigable:** Incluye imágenes, métricas claras y controles simples de usar.

---

## ¿Cómo se construyó?

* **Limpieza de datos:** Usamos `pandas` para transformar las columnas de años a filas (`melt`) y poder filtrar la información limpiamente.
* **Dashboard visual:** Desarrollado con `streamlit` para crear los selectores, el slider y la visualización de datos sin complicarse con desarrollo web avanzado.

---

## Archivos del repositorio

* `final.py`: El script de Python con todo el código del dashboard.
* `datos_ocde.csv`: La base de datos de origen con los indicadores.
* `assets/`: Carpeta con los recursos visuales (logos e imágenes).
* `requirements.txt`: Lista de librerías requeridas para ejecutar la app.

---
Cristian Gatica
Eloy Cisterna
