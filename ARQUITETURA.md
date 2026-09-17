# Arquitetura do Sistema

## Visão geral

O sistema utiliza uma arquitetura baseada em comunicação por mensagens.

O produtor envia mensagens para o RabbitMQ, que disponibiliza essas mensagens para o consumidor.

## Componentes

### Producer

O `producer.py` é responsável por enviar mensagens de pagamento para o RabbitMQ.

### RabbitMQ

O RabbitMQ funciona como intermediário entre o produtor e o consumidor, armazenando as mensagens na fila.

### Consumer

O `consumer.py` recebe as mensagens da fila e realiza o processamento.

## Fluxo

```text
Producer
   |
   | Envia mensagem
   v
RabbitMQ
   |
   | Entrega mensagem
   v
Consumer
   |
   v
Processamento