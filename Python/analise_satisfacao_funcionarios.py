import pandas as pd


caminhoarquivo = "/Users/ricardo/Documents/Tech/Data/Dataset/Analises/Recursos Humanos/Base de dados/HRDadosLimpos.xlsx"


df = pd.read_excel(caminhoarquivo)


print(df.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




plt.figure(figsize=(10, 10))  
sns.countplot(y=df["Satisfação Funcionario"], palette="coolwarm", order=df["Satisfação Funcionario"].value_counts().index)  # Ordenado por frequência


plt.title("Número de Funcionários por satisfação de trabalho")
plt.xlabel("Número de Funcionários")
plt.ylabel("Satisfação Funcionario")


plt.show()
