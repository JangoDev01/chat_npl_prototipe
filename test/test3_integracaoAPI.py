"""
    pip3 install pyTelegramBotAPI
        - Biblioteca para criar bots no Telegram.
    pip3 install telebot
        - Biblioteca alternativa para criar bots no Telegram.
    pip3 install python-decouple
        - Biblioteca para gerenciar variáveis de ambiente de forma segura.
"""

import telebot 

"""
    from decouple import config:
        - Importa a função 'config' da biblioteca 'decouple' para acessar variáveis de ambiente.
        - Permite que o token do bot seja armazenado de forma segura em um arquivo .env, evitando expor informações sensíveis no código.

"""
from decouple import config

"""
    
"""
token = config('TOKENBOT_TESTE')
bot = telebot.TeleBot(token)

###### PRIMEIRA ETAPA - Start Bot ######

# Define um manipulador de mensagens para o comando "/start". Quando um usuário enviar esse comando, a função 'start' será chamada...
@bot.message_handler(commands=["start"])

# A função 'start' é responsável por enviar uma mensagem de boas-vindas ao usuário...
def start(message):
    bot.send_message(message.chat.id, "Mekié nerd! Eu sou Beringelus o bot nerd. Como posso ajudar você hoje?", timeout=60)

# Faz uma sondagem contínua para verificar se há novas mensagens...
bot.polling()