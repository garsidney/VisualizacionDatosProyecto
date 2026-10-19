import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
df = pd.read_csv(r"C:\Users\Alexandra\Downloads\Software_Defect_Prediction_Dataset.csv")

# Configuración de estilo
sns.set(style="whitegrid")

plt.figure(figsize=(10,6))

# Scatter plot mejorado
sns.scatterplot(
    x="loc",
    y="method_count",
    hue="defect_label",
    size="fan_out",
    data=df,
    alpha=0.7,  # transparencia para evitar saturación
    sizes=(40, 300),  # rango de tamaños más equilibrado
    edgecolor="black",  # bordes para distinguir puntos
    palette={"Buggy": "red", "Clean": "blue"}  # paleta intencional
)

# Título y etiquetas claras
plt.title("LOC vs Métodos (color=defect_label, tamaño=fan_out)", fontsize=14, weight="bold")
plt.xlabel("Líneas de código (LOC)", fontsize=12)
plt.ylabel("Número de métodos", fontsize=12)

# Ajuste de leyenda
plt.legend(title="Defectos / Fan-out", bbox_to_anchor=(1.05, 1), loc="upper left")

# Cuadrícula ligera
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
