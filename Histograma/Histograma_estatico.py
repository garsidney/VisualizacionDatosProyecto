import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
df = pd.read_csv(r"...\Software_Defect_Prediction_Dataset.csv")

# Configuración de estilo
sns.set(style="whitegrid")

plt.figure(figsize=(10,6))

# Histograma con colores diferenciados
sns.histplot(
    data=df,
    x="loc",
    hue="defect_label",
    bins=40,
    palette={"Buggy": "red", "Clean": "blue"},
    alpha=0.5,
    element="step"
)

# Añadir líneas KDE (curvas de densidad) para cada categoría
sns.kdeplot(
    data=df[df["defect_label"]=="Buggy"]["loc"],
    color="red",
    linewidth=2,
    label="Tendencia Buggy"
)

sns.kdeplot(
    data=df[df["defect_label"]=="Clean"]["loc"],
    color="blue",
    linewidth=2,
    label="Tendencia Clean"
)

# Título y etiquetas
plt.title("Distribución del tamaño de archivos por defectos", fontsize=14, weight="bold")
plt.xlabel("Tamaño de archivo (LOC)")
plt.ylabel("Número de archivos")

# Leyenda
plt.legend(title="Defectos")

plt.show()