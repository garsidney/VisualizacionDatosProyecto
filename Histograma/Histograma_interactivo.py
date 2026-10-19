import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\Alexandra\Downloads\Software_Defect_Prediction_Dataset.csv")

fig = px.histogram(
    df,
    x="loc",
    nbins=40,
    color="defect_label",
    barmode="overlay",  # superposición para comparar distribuciones
    opacity=0.7,        # transparencia para legibilidad
    title="Distribución interactiva del tamaño de archivos por defectos",
    labels={"loc":"Tamaño de archivo (LOC)", "defect_label":"Defectos"}
)

# Ajustes de diseño
fig.update_layout(
    xaxis=dict(range=[0, 3000]),
    xaxis_title="Tamaño de archivo (LOC)",
    yaxis_title="Número de archivos",
    legend_title="Defectos",
    bargap=0.05,
    template="plotly_white"
)

fig.show()