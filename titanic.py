import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados do Titanic
titanic_data = pd.read_csv('caminho/do/arquivo/train.csv')

# Visualizando as primeiras linhas do DataFrame
st.write(titanic_data.head())

# Estatísticas gerais da base
st.subheader("Estatísticas Gerais:")
st.write(titanic_data.describe())

# Contagem de valores para algumas colunas
st.subheader("Contagem de Valores:")
st.write(titanic_data['Sex'].value_counts())
st.write(titanic_data['Pclass'].value_counts())
st.write(titanic_data['Embarked'].value_counts())

# Gráfico de barras para a contagem de sobreviventes
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', data=titanic_data, palette="Set2")
plt.title('Contagem de Sobreviventes no Titanic')
st.pyplot()

# Exibindo o gráfico
st.pyplot()