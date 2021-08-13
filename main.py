import os
import discord
from tortura import keep_alive

client = discord.Client()

# Token do Bot
my_secret = os.environ['thetoken']

# Atividade no perfil dele
client = discord.Client(activity=discord.Game(name='em desenvolvimento'))

# Lista de agradecimentos
agradecimentos = ["obrigado","brigado","brigadão","valeu"]
# Implementação futura de um sistema de agradecimentos, pra pontuar os membros que se dispôem a ajudar os outros. Uma lista assim também pode ser utilizada para filtrar palavras ofensivas.

# Mensagem de 'Pronto'
@client.event
async def on_ready():
  print('Bot logado como {0.user} e pronto para uso.'.format(client))

# Comandos de mensagens:
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
    # HELLO WORLD
    if message.content.startswith('!helloworld'): 
      await message.channel.send('Aqui está um exemplo de **Hello world!**, um código básico escrito em **C**, criado para exibir uma única mensagem:\n```c\n#include <stdio.h>\nint main(){\n\n    printf("kakaka iai men");\n    return 0;\n}```')
    # AJUDA
    if message.content.startswith('!ajuda'):
      await message.channel.send('Caso tenha dúvidas com alguma matéria, marque um **monitor** dessa matéria no canal referente a ela.\nMas se sua dúvida seja relacionada a algo do servidor, marque alguém da **Organização** do servidor no canal #geral, que a gente responde assim que possível.')

# IMPLEMENTAÇÕES FUTURAS
# Respostas automáticas a mensagens no chat
# Pins automáticos por reações de "⭐"

keep_alive()

client.run(os.getenv('thetoken'))