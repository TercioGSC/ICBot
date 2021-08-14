import os
import discord
from tortura import keep_alive

client = discord.Client()

# Token do Bot
my_secret = os.environ['thetoken']

# Atividade no perfil dele
client = discord.Client(activity=discord.Game(name='em desenvolvimento'))

# Lista de agradecimentos
agradecimentos = [
    "obrigado",
    "brigado",
    "brigadão",
    "valeu",
    "vlw",
]

# Lista de profanidades
bad_words = ["matar você"]
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
            await message.reply(
                'Aqui está um exemplo de **Hello world!**, um código básico escrito em **C**, criado para exibir uma única mensagem:\n```c\n#include <stdio.h>\nint main(){\n\n    printf("kakaka iai men");\n    return 0;\n}```'
            )
        # AJUDA
        if message.content.startswith('!ajuda'):
            await message.reply(
                'Caso tenha dúvidas com alguma matéria, marque um **monitor** dessa matéria no canal referente a ela.\nMas se sua dúvida seja relacionada a algo do servidor, marque alguém da **Organização** do servidor no canal #geral, que a gente responde assim que possível.'
            )
        # CONVITE PARA O SERVER(constante)
        if message.content.startswith('!convite'):
            await message.reply(
                f'Olá {message.author.mention}, aqui está o link de convite para o servidor:\n https://discord.gg/TBKwV2BKQg'
            )

# Respostas automáticas
# HELLO - Descobrir como fazer para o bot ler APENAS a palavra, não a combinação de caracteres em qualquer situação

        if "hello" in message.content.split():
            await message.reply('Hello world!')
        # ⭐ Easter Egg - Factorio
        if "factorio" in message.content.lower().split():
            await message.reply(
                '***"Alguém falou em Factorio?"***\n- Ancelmo, 2021')
        # ⭐ Easter Egg - Recursão
        if "recursão" in message.content.lower().split():
            await message.reply('**Você quis dizer *recursão*.**')

        # Lista - Agradecimentos
        if any(word in message.content.lower() for word in agradecimentos):
            await message.reply('De nada! Você é um amigo, amigo!')

        # Lista - Bad Words
        # Possível solução para as variedades de case das palavras: https://stackoverflow.com/questions/65480624/using-discord-py-to-filter-out-bad-words-no-other-commands-will-work
        if any(word in message.content.lower() for word in bad_words):
            await message.delete() # Apaga a mensagem...
            await message.channel.send(
                f'{message.author.mention}, se você continuar, vai ser mutado permanentemente no servidor.' # E responde ao usuário
            )

# IMPLEMENTAÇÕES FUTURAS
# Funcionalidade de "Procurando Grupo"
# Pins automáticos por reações de "⭐"

keep_alive()

client.run(os.getenv('thetoken'))
