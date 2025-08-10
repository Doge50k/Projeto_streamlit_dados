# Pipeline de Dados com Python, Docker e Streamlit 🚀

Este projeto de estudo demonstra a construção de um pipeline de dados simples e funcional. O sistema foi arquitetado para extrair dados de uma API pública, armazená-los em um banco de dados PostgreSQL e, por fim, exibi-los em um dashboard interativo construído com Streamlit.

Todo o ambiente é orquestrado com Docker e Docker Compose, garantindo que os serviços sejam isolados, reproduzíveis e fáceis de executar.

## Arquitetura do Sistema

O fluxo de dados segue uma arquitetura de serviços desacoplada, onde cada componente tem uma responsabilidade única:

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.9
-   **Banco de Dados:** PostgreSQL
-   **Dashboard:** Streamlit
-   **Containerização:** Docker & Docker Compose
-   **Bibliotecas Python Principais:**
    -   `requests` para as chamadas à API
    -   `SQLAlchemy` para a interação com o banco de dados
    -   `pandas` para a manipulação dos dados no dashboard
    -   `python-dotenv` para o gerenciamento de variáveis de ambiente

## 📁 Estrutura do Projeto

A organização dos arquivos foi pensada para manter os serviços desacoplados:

```bash
/
├── extractor/                # Serviço de extração e carga (ETL)
│   ├── Dockerfile
│   ├── extract_and_load.py
│   └── requirements.txt
│
├── dashboard/                # Serviço de visualização (Dashboard)
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── img/                      # Pasta para imagens do README
│   └── fluxograma-colorido.png
│   └── dashboard-screenshot.png
│
├── .env                      # Arquivo para variáveis de ambiente (local)
├── docker-compose.yml        # Orquestrador dos contêineres
└── README.md                 # Documentação do projeto

````
## ✅ Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina:
- Docker
- Docker Compose

## 🚀 Como Executar o Projeto
Siga os passos abaixo para rodar a aplicação localmente:

1. **Clone o repositório:**

```bash
git clone https://github.com/Doge50k/Projeto_streamlit_dados.git
cd Projeto_streamlit_dados
````

2. **Crie o arquivo de variáveis de ambiente:**
Crie um arquivo chamado .env na raiz do projeto e cole o seguinte conteúdo. Ele será usado para configurar o banco de dados.

```bash
# Credenciais do PostgreSQL
POSTGRES_DB=minha_base_de_dados
POSTGRES_USER=meu_usuario
POSTGRES_PASSWORD=minha_senha
````

3. **Construa e inicie os contêineres:**
Este comando irá construir as imagens Docker para cada serviço e iniciar todos os contêineres em segundo plano.
```bash
docker-compose up --build
````
O script de extração rodará automaticamente após o banco de dados estar pronto.

4. **Acesse o Dashboard:**
Após a inicialização dos contêineres, abra seu navegador e acesse:
[http://localhost:8501](http://localhost:8501)

6. **Para para a aplicação:**
Para parar todos os contêineres, pressione Ctrl + C no terminal onde o docker-compose está rodando, ou execute o seguinte comando em outro terminal (na mesma pasta):
```bash
docker-compose down
````

## 💡 Próximos Passos
Este projeto serve como uma base sólida. Algumas melhorias e próximos passos possíveis incluem:

- [ ] Agendar a execução do script de extração periodicamente (usando cron ou um orquestrador como Airflow).
- [ ] Adicionar tratamento de erros e um sistema de logs mais robusto.
- [ ] Implementar testes unitários e de integração.
- [ ] Adicionar mais filtros e gráficos interativos ao dashboard.
- [ ] Criar um pipeline de CI/CD para automatizar o deploy.

Feito por [Elias](https://github.com/Doge50k)
