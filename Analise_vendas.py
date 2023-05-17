import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("VENDAS.xlsx")

status_count = df['STATUS'].value_counts()
cliente_count = df['CLIENTE'].value_counts()
produto_count = df['PRODUTO'].value_counts()
estado_count = df['ESTADO'].value_counts().head(10)
idade_count = df['IDADE'].value_counts().head(20)
cep_count = df['CEP'].value_counts().head(10)

# Cria a figura e os subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Primeiro gráfico
estado_count.plot(kind='bar', ax=ax1)
ax1.set_xlabel('Estado')
ax1.set_ylabel('Número de Vendas')
ax1.set_title('Vendas por Estado')

# Segundo gráfico
idade_count.plot(kind='bar', ax=ax2)
ax2.set_ylabel('Idade')
ax2.set_xlabel('Número de Vendas')
ax2.set_title('Vendas por Idade')

# Ajusta o espaçamento entre os subplots
plt.tight_layout()

# Exibe a figura com os dois gráficos
plt.show()
