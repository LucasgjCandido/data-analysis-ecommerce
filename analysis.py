import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv("dataset.csv")

# criar faturamento
df["faturamento"] = df["preco"] * df["quantidade"]

# métricas
faturamento_total = df["faturamento"].sum()
ticket_medio = df["faturamento"].mean()

print("Faturamento total:", faturamento_total)
print("Ticket médio:", ticket_medio)

# vendas por produto
produtos = df.groupby("produto")["quantidade"].sum()

# gráfico produtos
produtos.plot(kind="bar")
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_produtos.png")
plt.clf()

# vendas por categoria
categorias = df.groupby("categoria")["quantidade"].sum()

# gráfico categorias
categorias.plot(kind="bar")
plt.title("Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("grafico_categorias.png")
