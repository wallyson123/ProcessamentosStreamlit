import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados do Titanic
@st.cache(allow_output_mutation=True)
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    data = pd.read_csv(url)
    return data

# Função para exibir estatísticas gerais
def show_general_stats(data):
    st.subheader("Estatísticas Gerais")
    st.write(f"Total de Passageiros: {len(data)}")
    st.write(f"Total de Sobreviventes: {data['Survived'].sum()}")
    st.write(f"Total de Não Sobreviventes: {len(data) - data['Survived'].sum()}")
    st.write(f"Taxa de Sobrevivência: {data['Survived'].mean() * 100:.2f}%")

# Função para exibir contagem de valores
def show_value_counts(data, column):
    st.subheader(f"Contagem de Valores para {column}")
    value_counts = data[column].value_counts()
    st.bar_chart(value_counts)

# Função para exibir gráfico de barras
def show_bar_chart(data, x, y, title):
    st.subheader(title)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, data=data)
    st.pyplot()

def main():
    st.title("Análise de Dados do Titanic")
    data = load_data()

    # Sidebar com opções
    st.sidebar.title("Opções")
    selected_chart = st.sidebar.selectbox("Escolha o Gráfico", ["Contagem de Sobreviventes", "Idade por Classe"])

    # Exibir estatísticas gerais
    show_general_stats(data)

    # Exibir gráfico selecionado
    if selected_chart == "Contagem de Sobreviventes":
        show_value_counts(data, "Survived")
    elif selected_chart == "Idade por Classe":
        show_bar_chart(data, "Pclass", "Age", "Idade por Classe")

if __name__ == "__main__":
    main()