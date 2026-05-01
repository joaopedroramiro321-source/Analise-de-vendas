import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# =================================
# LEITURA DOS DADOS
# =================================

df = pd.read_csv("vendas_projeto.csv")

# =================================
# EXPLORAÇÃO DOS DADOS
# =================================

df.head()
df.info()
df.describe()

# =================================
# ANÁLISE DOS DADOS
# =================================
df["faturamento"] = df["preco"] * df["quantidade"]

#Faturamento por categoria
faturamento_categoria = df.groupby("categoria")["faturamento"].sum()
print(faturamento_categoria)

#Faturamento total
print("Faturamento total: ", df["faturamento"].sum())

#Produto mais vendido
produto_mais_vendido = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(5)
print(produto_mais_vendido)

#Produto mais lucrativo
mais_lucrativo = df.groupby("produto")["faturamento"].sum().sort_values(ascending=False)
print(mais_lucrativo) 

# =================================
# VISUALIZAÇÃO DOS DADOS
# =================================

#Gráfico de faturamento por categoria
faturamento_categoria.plot(kind="bar")

plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento")

plt.show()

#Gráfico de produtos com mais faturamento
mais_lucrativo.head(5).plot(kind="bar")

plt.title("Top Produtos por Faturamento")

plt.show()

#Gráfico de produtos mais vendidos
produto_mais_vendido.head(5).plot(kind="bar")

plt.title("Produtos mais vendidos")
plt.show()