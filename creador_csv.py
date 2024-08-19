import pandas as pd

print(print(pd.__version__))
# Dataframe es la informacion basica con el nombre de las piezas y centimetros para poder armar el Excel

data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros" : [40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)

