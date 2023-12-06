import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados do Titanic
titanic_data = pd.read_csv('C:/testtitanic/train.csv')

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
plt.figure(figsize=(12, 6))

# Contagem de sobreviventes por classe
plt.subplot(2, 3, 1)
sns.countplot(x='Survived', hue='Pclass', data=titanic_data, palette="Set2")
plt.title('Contagem de Sobreviventes por Classe')

# Distribuição de idades
plt.subplot(2, 3, 2)
sns.histplot(titanic_data['Age'].dropna(), kde=True, bins=30, color='blue')
plt.title('Distribuição de Idades')

# Contagem de sobreviventes por sexo
plt.subplot(2, 3, 3)
sns.countplot(x='Survived', hue='Sex', data=titanic_data, palette="Set2")
plt.title('Contagem de Sobreviventes por Sexo')

# Contagem de embarques por local
plt.subplot(2, 3, 4)
sns.countplot(x='Embarked', data=titanic_data, palette="Set2")
plt.title('Contagem de Embarques por Local')

# Distribuição de tarifas
plt.subplot(2, 3, 5)
sns.histplot(titanic_data['Fare'], kde=True, bins=30, color='green')
plt.title('Distribuição de Tarifas')

plt.tight_layout()
plt.show()