import pika

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (se ela não existir, será criada)
channel.queue_declare(queue='fila_tarefas')

# Mensagem que será enviada
mensagem = 'Processar pedido de Rodrigo Shodi Sumioshi#1234'

# Publicar a mensagem na fila
channel.basic_publish(exchange='',
                      routing_key='fila_tarefas',
                      body=mensagem)

print(f" [x] Enviado '{mensagem}'")

# Fechar a conexão
connection.close()
