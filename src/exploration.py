import pandas as pd

# Cargar el dataset
data = pd.read_csv('data/data.csv')

# Detectar valores faltantes
missing_values = data.isnull().sum()
print("Valores faltantes por columna:\n", missing_values)

# Guardar el resultado de valores faltantes en un archivo
with open('data/missing_values.txt', 'w') as f:
    f.write(str(missing_values))

