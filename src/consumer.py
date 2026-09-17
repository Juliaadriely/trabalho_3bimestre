import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials("admin", "admin")
    )
)

channel = connection.channel()

channel.queue_declare(queue="pagamentos", durable=True)


def receber_mensagem(ch, method, properties, body):
    mensagem = json.loads(body)

    print("Pagamento recebido:")
    print(f"ID: {mensagem['pagamento_id']}")
    print(f"Status: {mensagem['status']}")
    print(f"Valor: R$ {mensagem['valor']:.2f}")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue="pagamentos",
    on_message_callback=receber_mensagem,
    auto_ack=False
)

print("Aguardando pagamentos...")

channel.start_consuming()

def receber_mensagem(ch, method, properties, body):
    print("Processando mensagem...")

    mensagem = json.loads(body)

    print("Pagamento recebido:")
    print(f"ID: {mensagem['pagamento_id']}")
    print(f"Status: {mensagem['status']}")
    print(f"Valor: R$ {mensagem['valor']:.2f}")

    ch.basic_ack(delivery_tag=method.delivery_tag)