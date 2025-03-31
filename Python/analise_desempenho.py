import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


caminho_arquivo = "/Users/ricardo/Documents/Tech/Data/Dataset/Analises/Recursos Humanos/Base de dados/HRDadosLimpos.xlsx"


df = pd.read_excel(caminho_arquivo)


if "Satisfação Funcionario" in df.columns:
    
    plt.figure(figsize=(8, 8))
    df["Satisfação Funcionario"].value_counts().plot.pie(
        autopct="%1.1f%%",
        colors=sns.color_palette("viridis", len(df["Satisfação Funcionario"].unique()))
    )

    plt.title("Distribuição de funcionários por satisfaçãode trabalho")
    plt.ylabel("")  
    plt.show()
else:
    print("A coluna 'EstadoCivil' não foi encontrada no DataFrame.")
