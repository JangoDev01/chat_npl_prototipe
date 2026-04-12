import telebot, csv
import time
from decouple import config
from datetime import datetime

token = config('TOKENBOT_TESTE')
bot = telebot.TeleBot(token)

###### SEGUNDA ETAPA - Salvar dados ######

"""
    funcao pra salvar os dados da conversa do bot com o usuario em um arquivo csv.
    para isso é necessário importar a biblioteca csv e criar a função salvar_dados.
    que recebe como parâmetros o nome do arquivo e a conversa em formato de lista. 
    A função abre o arquivo em modo de escrita (append) e utiliza o objeto csv.writer para escrever a conversa no arquivo.
"""
def salvar_dados(arquivo, conversa: list):
    with open(arquivo, 'a') as chat:
        e = csv.writer(chat)
        e.writerow(conversa)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Mekié nerd! Eu sou Beringelus o bot nerd que irá te ajudar a ler quadrinhos e livros.")
    time.sleep(3)
    bot.send_message(message.chat.id, "Eis o nosso menu de opções de Quadrinhos e Livros para a sua degustação nerd:")
    time.sleep(5)
    bot.send_message(message.chat.id, "- Quadrinhos da Marvel.\n- Quadrinhos da DC.\n- Manga.\n- Manhwa.\n- Quadrinhos de terror.\n- Livros de Fantasia.")


@bot.message_handler(regexp=r"Marvel|DC|Manga|Manhwa|Quadrinhos de terror|Livros de Fantasia")
def responder_nerd(message):
    topicos = []

    # teste para ver tudo o que tem dentro da mensagem entre o bot e o usuario...
    print(message)
    salvar_dados("test/doc/conversa.csv", [message.chat.id,message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text, datetime.now().strftime("%d-%m-%Y %H:%M:%S")])

    for topico in ["Marvel", "DC", "Manga", "Manhwa", "Quadrinhos de terror", "Livros de Fantasia"]:
        if topico.lower() in message.text.lower():
            topicos.append(topico)

    if topicos:
        bot_msg = f"Ah, você gosta de {', '.join(topicos)}! Bora ver o que temos pra vc!"
        bot_msg2 = (f"OBS: não importa o que vc digitar o documento carregado será sempre o mesmo...")
        bot_msg3 = (f"Bem, eu sou apenas um Bot de teste, o que vc queria que eu fizesse? kkkkkk")
        bot_msg4 = (f"Agora que todas as cartas estão na mesa, ainda queres continuar..?")
    else:
        bot_msg = "Desculpe, não consegui entender o tópico. Pode tentar novamente?"

    bot.send_message(message.chat.id, bot_msg)
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

    doc = open("test/doc/Cap_1.cbz", "rb")

    if confirm:
        bot_msg1 = f"Ótimo! Preparando o documento pro download..."
        bot_msg2 = f"O documento está pronto..."
    else:
        bot_msg = "Entendi, se quiser baixar o documento é só me avisar!"

    bot.send_message(message.chat.id, bot_msg1)
    time.sleep(7)
    bot.send_message(message.chat.id, bot_msg2)
    bot.send_document(message.chat.id, doc)
    time.sleep(5)
    bot.send_message(message.chat.id, "Tenha uma ótima degustação... Seu nerd!")

# Faz uma sondagem contínua para verificar se há novas mensagens...
bot.polling()