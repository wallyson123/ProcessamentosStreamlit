import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados do Titanic
titanic_data = pd.read_csv('train.csv')

# Visualizando as primeiras linhas do DataFrame
print(titanic_data.head())

# Estatísticas gerais da base
print("\nEstatísticas Gerais:")
print(titanic_data.describe())

# Contagem de valores para algumas colunas
print("\nContagem de Valores:")
print(titanic_data['Sex'].value_counts())
print(titanic_data['Pclass'].value_counts())
print(titanic_data['Embarked'].value_counts())

# Gráfico de barras para a contagem de sobreviventes
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', data=titanic_data, palette="Set2")
plt.title('Contagem de Sobreviventes no Titanic')
plt.show()