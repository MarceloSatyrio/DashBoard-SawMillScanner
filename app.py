import pandas as pd
import streamlit as st
from datetime import date
import git
import os

# Definir a configuração da página
st.set_page_config(layout="wide")

# Permitir que o usuário selecione a data desejada
data_selecionada = st.date_input("Selecione a data desejada:", date.today(), min_value=date(2020, 1, 1), max_value=date.today())

# Transformar a data selecionada em uma string no formato 'YYYY-MM-DD'
data_formatada = data_selecionada.strftime("%Y-%m-%d")

# Clonar o repositório do GitHub para uma pasta temporária
repo_url = 'https://github.com/MarceloSatyrio/dashboard-SawMillScanner.git'
temp_folder = '/tmp/git_repo'  # Pasta temporária para clonar o repositório

try:
    # Clonar o repositório do GitHub para a pasta temporária
    git.Repo.clone_from(repo_url, temp_folder)

    # Construir o caminho do arquivo correspondente à data selecionada
    arquivo_selecionado = os.path.join(temp_folder, f"{data_formatada}_DadosProd.xlsx")

    # Carregar os dados do arquivo Excel selecionado
    df = pd.read_excel(arquivo_selecionado)

    # Certifique-se de que 'Date' (ou 'Data') é uma coluna de data
    if 'Date' in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    elif 'Data' in df.columns:
        df["Date"] = pd.to_datetime(df["Data"])
    else:
        st.error("A coluna de data não foi encontrada no DataFrame.")

    # Remover a última coluna 'Date' da tabela
    if 'Date' in df.columns:
        df = df.drop(columns=['Date'])

    # Iniciar o aplicativo Streamlit
    st.title("Meu Dashboard")

    # Adicionar um dataframe ao dashboard (exibindo as primeiras linhas)
    st.write("Dados do DataFrame:")
    st.write(df.head())
except git.GitCommandError as e:
    st.error(f"Erro ao clonar o repositório: {e}")
except FileNotFoundError:
    st.error(f"Nenhum arquivo de dados encontrado para a data {data_formatada}.")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
