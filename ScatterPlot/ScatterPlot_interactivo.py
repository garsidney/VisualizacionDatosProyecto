import plotly.express as px
import pandas as pd

# Cargar dataset
df = pd.read_csv(r"...\Software_Defect_Prediction_Dataset.csv")

# Crear nueva variable de ciclos
df["loop_count"] = df["for_loop_count"] + df["while_loop_count"]

# Scatter plot interactivo
fig = px.scatter(
    df,
    x="loc",
    y="cyclomatic_complexity",
    color="defect_label",
    size="fan_out",
    hover_data=["comment_density", "fan_in", "fan_out", "loop_count"],
    opacity=0.7,
    title="Relación interactiva LOC vs Complejidad ciclomática"
)

# Ajustes de diseño
fig.update_layout(
    xaxis_title="Líneas de código (LOC)",
    yaxis_title="Complejidad ciclomática",
    legend_title="Defectos",
    template="plotly_white"
)

fig.show()
