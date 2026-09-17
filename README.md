# Sistema de Pagamentos

## Descrição

Este projeto apresenta um sistema simples de processamento de pagamentos desenvolvido em Python, utilizando RabbitMQ para comunicação entre produtor e consumidor.

O produtor envia mensagens de pagamento para uma fila do RabbitMQ e o consumidor recebe e processa essas mensagens.

## Tecnologias utilizadas

- Python
- RabbitMQ
- Docker
- Docker Compose

## Estrutura do projeto

```text
trabalho_3bimestre/
├── src/
│   ├── producer.py
│   └── consumer.py
├── ARQUITETURA.md
├── CHANGELOG.md
├── docker-compose.yml
└── README.md