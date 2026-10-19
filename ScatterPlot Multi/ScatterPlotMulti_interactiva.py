import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\Alexandra\Downloads\Software_Defect_Prediction_Dataset.csv")

fig = px.scatter(
    df,
    x="loc",
    y="method_count",
    color="defect_label",
    size="fan_out",
    hover_data=["cyclomatic_complexity", "comment_density", "inheritance_depth"],
    title="Visualización interactiva multivariada"
)
fig.update_layout(xaxis_title="Líneas de código (LOC)", yaxis_title="Número de métodos")
fig.show()