import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


caminho_arquivo = "/Users/ricardo/Downloads/Recursos Humanos/Base de dados/HRDadosLimpos.xlsx"


df = pd.read_excel(caminho_arquivo)


print(df.head())


plt.figure(figsize=(9, 5))
sns.countplot(x=df["Departamento"], palette="viridis")


plt.title("Número de Funcionários por Departamento")
plt.xticks(rotation=45)
plt.xlabel("Departamento")
plt.ylabel("Número de Funcionários")

plt.show()
