import pika

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (deve ser a mesma usada no produtor)
channel.queue_declare(queue='fila_tarefas')

# Função que será chamada para processar cada mensagem
def callback(ch, method, properties, body):
    print(f" [x] Recebido {body}")
    # Aqui você pode colocar a lógica de processamento da tarefa
    print(" [x] Processando a mensagem...")

# Configurar o consumidor para ouvir a fila
channel.basic_consume(queue='fila_tarefas',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()

