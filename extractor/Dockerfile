FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiei o resto do código do nosso script para o contêiner.
COPY . .

# Comando que será executado quando o contêiner iniciar.
CMD ["python", "extract_and_load.py"]