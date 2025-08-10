FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expus a porta 8501, que é a porta padrão do Streamlit.
EXPOSE 8501

# O comando padrão para iniciar a aplicação Streamlit no arquivo app.py
CMD ["streamlit", "run", "app.py"]