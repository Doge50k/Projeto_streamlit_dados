import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Dashboard de Usuários",
    page_icon="👤",
    layout="wide"
)

# Pega as credenciais do banco de dados das variáveis de ambiente
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = "db"
DB_PORT = "5432"

# String de conexão com o banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Função para buscar os dados do banco.
@st.cache_data
def carregar_dados():
    try:
        engine = create_engine(DATABASE_URL)
        query = "SELECT * FROM usuarios;"
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Erro ao conectar ou buscar dados do banco: {e}")
        return pd.DataFrame() # Retorna um DataFrame vazio em caso de erro

# Construção da Página

st.title("👥 Dashboard de Usuários")
st.markdown("Este dashboard exibe dados de usuários extraídos de uma API e armazenados em um banco de dados PostgreSQL.")

# Carrega os dados
df_usuarios = carregar_dados()

if df_usuarios.empty:
    st.warning("Nenhum dado encontrado no banco de dados. O script de extração já foi executado?")
else:
    st.subheader("Visão Geral dos Usuários")
    
    # Exibe o número total de usuários
    total_usuarios = len(df_usuarios)
    st.metric(label="Total de Usuários", value=total_usuarios)

    st.subheader("Tabela de Dados")
    st.dataframe(df_usuarios, use_container_width=True)

    st.subheader("Visualizações")
    
    # Gráfico simples: contagem de usuários por website
    st.write("#### Contagem de Usuários por Domínio do Website")
    # Extrai o domínio do website para uma visualização mais limpa
    df_usuarios['domain'] = df_usuarios['website'].apply(lambda x: x.split('/')[0] if isinstance(x, str) else 'N/A')
    domain_counts = df_usuarios['domain'].value_counts()
    st.bar_chart(domain_counts)

# Botão para limpar o cache e recarregar os dados
if st.button('Recarregar Dados'):
    st.cache_data.clear()
    st.rerun()