# Servicio de Productos (products-service/Dockerfile):
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python3", "app.py"]
