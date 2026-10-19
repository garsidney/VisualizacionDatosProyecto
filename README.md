# Proyecto de Visualización de Datos - Software Defect Prediction

## 📌 Descripción
Este proyecto analiza el **Software Defect Prediction Dataset** (archivos fuente en Java con métricas de calidad de código) para responder la pregunta analítica:  
**¿Qué características del código (tokens, estructuras, atributos semánticos) están más asociadas con la presencia de bugs en proyectos Java, y cómo podemos construir un modelo predictivo confiable para anticiparlos?**

Todas las visualizaciones consideran la variable **`defect_label`** como referencia principal para diferenciar entre archivos *Buggy* y *Clean*.  
La métrica principal de tamaño de archivo es **`loc`** (líneas de código).

---

## 📂 Estructura del proyecto
- [Software Defect Prediction Dataset](https://www.kaggle.com/datasets/colabsss/software-defect-prediction-dataset?resource=download) → Dataset original con métricas de código.  
- `Dashboard Tableau/Dashboard.twb` → Dashboard realizado en herramienta Tableau  
- `Histograma/Histograma_estatico.py` → Gráficos estáticos (Matplotlib/Seaborn).  
- `Histograma/Histograma_interactivo.py/` → Gráficos interactivos (Plotly).
- `ScatterPlot/ScatterPlot_estatico.py` → Gráficos estáticos (Matplotlib/Seaborn).  
- `ScatterPlot/ScattterPlot_interactivo.py/` → Gráficos interactivos (Plotly).
- `ScatterPlot Multi/ScattterPlotMulti_estatico.py` → Gráficos estáticos (Matplotlib/Seaborn).  
- `ScatterPlot Multi/ScattterPlotMulti_interactivo.py/` → Gráficos interactivos (Plotly).   
- `README.md` → Documento de reproducibilidad y guía del proyecto.

---

## ⚙️ Requisitos
Instalar las siguientes librerías de Python:

```bash
pip install pandas matplotlib seaborn plotly

Descargar el dataset y cada .py ajustar la url de donde se encuentra para que sea tomado.
```
Descargar y actualizar la ruta de donde se guardo el dataset.
Cada archivo .py cuenta con esa seccion.
```python
# Cargar dataset
df = pd.read_csv(r"C:\Users\...\Downloads\Software_Defect_Prediction_Dataset.csv")
```