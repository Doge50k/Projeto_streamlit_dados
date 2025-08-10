import os
import time
import requests
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Pega as credenciais do banco de dados das variáveis de ambiente
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = "db"
DB_PORT = "5432"

# String de conexão com o banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Tenta conectar ao banco de dados. Às vezes, o script pode iniciar antes do banco
# Então fiz um loop de tentativas.
connection_attempts = 10
for i in range(connection_attempts):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        break
    except OperationalError as e:
        print(f"Não foi possível conectar ao banco de dados: {e}")
        if i < connection_attempts - 1:
            print("Tentando novamente em 5 segundos...")
            time.sleep(5)
        else:
            print("Falha ao conectar ao banco de dados após várias tentativas. Abortando.")
            exit(1)


# Define a estrutura da tabela de usuários
create_table_query = text("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    website VARCHAR(255)
);
""")

# Executa o comando para criar a tabela (se ela não existir)
with engine.connect() as connection:
    connection.execute(create_table_query)
    connection.commit()
    print("Tabela 'usuarios' verificada/criada com sucesso.")

def extrair_dados_api():
    """Função para extrair dados da API JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status() # Lança um erro se a requisição falhar (código != 200)
        print(f"Dados extraídos da API com sucesso! (Status: {response.status_code})")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao extrair dados da API: {e}")
        return None

def carregar_dados_no_banco(dados):
    """Função para carregar os dados no banco de dados."""
    if not dados:
        print("Nenhum dado para carregar.")
        return

    with engine.connect() as connection:
        for usuario in dados:
            # Verifica se o usuário já existe para não duplicar
            user_exists = connection.execute(text("SELECT id FROM usuarios WHERE id = :id"), {"id": usuario['id']}).scalar()

            if not user_exists:
                insert_query = text("""
                    INSERT INTO usuarios (id, name, username, email, phone, website)
                    VALUES (:id, :name, :username, :email, :phone, :website)
                """)
                connection.execute(insert_query, {
                    "id": usuario['id'],
                    "name": usuario['name'],
                    "username": usuario['username'],
                    "email": usuario['email'],
                    "phone": usuario['phone'],
                    "website": usuario['website']
                })
        connection.commit()
    print(f"{len(dados)} registros de usuários processados e carregados no banco de dados.")

if __name__ == "__main__":
    dados_usuarios = extrair_dados_api()
    if dados_usuarios:
        carregar_dados_no_banco(dados_usuarios)
        