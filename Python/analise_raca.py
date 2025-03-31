import pandas as pd

caminho_arquivo = "/Users/ricardo/Documents/Tech/Data/Dataset/Analises/Recursos Humanos/Base de dados/HRDadosLimpos.xlsx"

df = pd.read_excel(caminho_arquivo)

print(df.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 10))  
sns.countplot(y=df["Raca"], palette="coolwarm", order=df["Raca"].value_counts().index) 

plt.title("Número de Funcionários por Raca")
plt.xlabel("Número de Funcionários")
plt.ylabel("Raca")

plt.show()
