import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

caminho_arquivo = "https://raw.githubusercontent.com/ricardogeorgeam/Database/refs/heads/main/Chocolate%20Sales.csv"

df = pd.read_csv(caminho_arquivo)


duplicados = df[df.duplicated()]
print(duplicados)


num_duplicados = df.duplicated().sum()
print(f'Número de duplicatas: {num_duplicados}')



