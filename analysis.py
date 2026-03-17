import pandas as pd

# carregar dados
df = pd.read_csv("dataset.csv")

# criar coluna faturamento
df["faturamento"] = df["preco"] * df["quantidade"]

# faturamento total
faturamento_total = df["faturamento"].sum()

# ticket médio
ticket_medio = df["faturamento"].mean()

# produtos mais vendidos
top_produtos = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)

print("Faturamento total:", faturamento_total)
print("Ticket médio:", ticket_medio)
print("\nProdutos mais vendidos:")
print(top_produtos)
