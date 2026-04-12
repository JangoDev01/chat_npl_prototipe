"""
    pip3 install pyTelegramBotAPI
        - Biblioteca para criar bots no Telegram.
    pip3 install telebot
        - Biblioteca alternativa para criar bots no Telegram.
    pip3 install python-decouple
        - Biblioteca para gerenciar variáveis de ambiente de forma segura.
"""

import telebot
import time

"""
    from decouple import config:
        - Importa a função 'config' da biblioteca 'decouple' para acessar variáveis de ambiente.
        - Permite que o token do bot seja armazenado de forma segura em um arquivo .env, evitando expor informações sensíveis no código.

"""
from decouple import config

token = config('TOKENBOT_TESTE')
bot = telebot.TeleBot(token)

###### PRIMEIRA ETAPA - Start Bot ######

# Define um manipulador de mensagens para o comando "/start". Quando um usuário enviar esse comando, a função 'start' será chamada...
@bot.message_handler(commands=["start"])

# A função 'start' é responsável por enviar uma mensagem de boas-vindas ao usuário...
def start(message):
    bot.send_message(message.chat.id, "Mekié nerd! Eu sou Beringelus o bot nerd que irá te ajudar a ler quadrinhos e livros.")
    time.sleep(3)
    bot.send_message(message.chat.id, "Eis o nosso menu de opções de Quadrinhos e Livros para a sua degustação nerd:")
    time.sleep(5)
    bot.send_message(message.chat.id, "- Quadrinhos da Marvel.\n- Quadrinhos da DC.\n- Manga.\n- Manhwa.\n- Quadrinhos de terror.\n- Livros de Fantasia.")

"""
    Define um manipulador de mensagens que responde a mensagens contendo palavras-chave relacionadas a temas nerds.
    O parâmetro 'regexp' é usado para especificar uma expressão regular que corresponde a essas palavras-chave.
    Quando um usuário enviar uma mensagem que corresponda a essa expressão regular, a função 'responder_nerd' será chamada...
    a função 'responder_nerd' é responsável por:
         - enviar uma mensagem de resposta personalizada ao usuário, reconhecendo o interesse dele por temas nerds.
         - caso o topico esteja no meio de uma frase:
            - a função irá extrair o tópico específico da mensagem do usuário usando a expressão regular.
            - em seguida, enviará uma resposta personalizada mencionando o tópico específico, mostrando que o bot entendeu o interesse do usuário.
            - ao dar uma resposta personalizada, o bot não deve repetir a frase toda que o usuario digitou junto com o topico, 
              mas sim apenas o topico específico, para evitar respostas repetitivas e tornar a interação mais fluida.
"""
@bot.message_handler(regexp=r"Marvel|DC|Manga|Manhwa|Quadrinhos de terror|Livros de Fantasia")
def responder_nerd(message):
    topicos = [] # Lista para armazenar os tópicos encontrados na mensagem do usuário.

    """
        Loop para verificar se cada tópico da lista de tópicos nerds está presente na mensagem do usuário.
        Se um tópico for encontrado, ele é adicionado à lista 'topicos'.
         - A verificação é feita usando o método 'lower()' para garantir que a comparação seja case-insensitive.
    """
    for topico in ["Marvel", "DC", "Manga", "Manhwa", "Quadrinhos de terror", "Livros de Fantasia"]:
        if topico.lower() in message.text.lower():
            topicos.append(topico)

    if topicos:
        # join - método usado para criar uma string a partir dos tópicos encontrados, separando-os por vírgulas.
        bot_msg = f"Ah, você gosta de {', '.join(topicos)}! Bora ver o que temos pra vc!"
        bot_msg2 = (f"OBS: não importa o que vc digitar o documento carregado será sempre o mesmo...")
        bot_msg3 = (f"Bem, eu sou apenas um Bot de teste, o que vc queria que eu fizesse? kkkkkk")
        bot_msg4 = (f"Agora que todas as cartas estão na mesa, ainda queres continuar..?")
    else:
        bot_msg = "Desculpe, não consegui entender o tópico. Pode tentar novamente?"

    bot.send_message(message.chat.id, bot_msg)  # Envia a resposta personalizada ao usuário.  bot.send_message(message.chat.id, bot_msg)  # Envia a resposta personalizada ao usuário.
    time.sleep(5)
    bot.send_message(message.chat.id, bot_msg2)
    time.sleep(5)
    bot.send_message(message.chat.id, bot_msg3)
    time.sleep(5)
    bot.send_message(message.chat.id, bot_msg4)

@bot.message_handler(regexp=r"Claro|Sim|Quero|To afim|Sem makas|na boa|Pode ser|Por mim tudo bem|Yha|Fix|Fechado|Bora|Na boa")
def donwload(message):
    confirm = []
    for resposta in ["Claro", "Sim", "Quero", "To afim", "Sem makas", "na boa", 
                     "Pode ser", "Por mim tudo bem", 
                     "Yha", "Fix", "Fechado", "Bora", "Na boa"]:
        if resposta.lower() in message.text.lower():
            confirm.append(resposta)

    doc = open("test/doc/Cap_1.cbz", "rb")  # Abre o arquivo do documento em modo de leitura binária.

    if confirm:
        bot_msg1 = f"Ótimo! Preparando o documento pro download..."
        bot_msg2 = f"O documento está pronto..."
    else:
        bot_msg = "Entendi, se quiser baixar o documento é só me avisar!"

    bot.send_message(message.chat.id, bot_msg1)
    time.sleep(7)
    bot.send_message(message.chat.id, bot_msg2)
    bot.send_document(message.chat.id, doc)  # Envia o documento para o usuário usando o método 'send_document' do bot.
    time.sleep(5)
    bot.send_message(message.chat.id, "Tenha uma ótima degustação... Seu nerd!")

# Faz uma sondagem contínua para verificar se há novas mensagens...
bot.polling()