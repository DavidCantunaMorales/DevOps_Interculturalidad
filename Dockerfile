# Etapa 1: Construcción con Ubuntu
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev && \
    pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# Etapa 2: Imagen final con Alpine
FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache libstdc++ musl-dev gcc

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 5000
COPY wait-for-mysql.sh /wait-for-mysql.sh
CMD ["/wait-for-mysql.sh"]

