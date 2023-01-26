import requests
import json
import telebot
import time
import os

previous_data = None   # NAO ALTERAR
expected = 0           # NAO ALTERAR
cor_atual = "Q"        # NAO ALTERAR
analise_sinal = False  # NAO ALTERAR
banca = 100            # NAO ALTERAR
entrada = 0            # NAO ALTERAR
erros = 0              # NAO ALTERAR
acertos = 0            # NAO ALTERAR
max_gale = 2           # ALTERE PARA O NUMERO MAXIMO DE GALE

token = '5887698775:AAGr19dJlRNI3qoREEu7R_F1OBIRnhhuyY4kSzs' # BOT TOKEN
chat_id = '-10017365610tt616' # CHAT ID DO CANAL ONDE DESEJA ENVIAR MSG

bot = telebot.TeleBot(token)
bot.send_sticker(chat_id, 'CAACAgEAAxkBAAEHWbFjybxJtejWQ677CjHN8Batt55A8PoZngAC0QEAAo6ouERzvaHhBTM6eC0E')

def enviarMenssagem(text):  # recebe um texto,
    url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url_base)


enviarMenssagem('''
No site https://midsetpro.com.br/ é possível ter acesso ao código fonte do robô da blazer comercialmente para que os usuários possam montar seus próprios canais de sinais da blazer.

⚠️ VISITE O SITE E MONTE SEU PRÓPRIO GRUPO DE SINAIS ⚠️

''')

def enviar_sinal(cor, padrao):
    global banca
    global entrada
    global cor_atual
    cor_atual = cor

    p1 = "🟢 𝗦𝗜𝗡𝗔𝗟 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗢 🟢"
    p2 = "🟢 Padrão:" + padrao
    p3 = "🎯Entrada:" + cor_atual
    p4 = "🦾proteger no ⚪️"
    p5 = "🐓2 martingale: (opcional)"
    p6 = "⚠️ 𝗔𝗹𝗲𝗿𝘁𝗮: Entre até o 2x Martingale"
    p7 = "Dobre a aposta em cada Gale"
    p8 = "Ao ganhar espera o proximo sinal !!"
    p9 = "⚠️ Atenção: visite o meu website\n\nhttps://midsetpro.com.br/"

    enviarMenssagem(p1+"\n\n"+p2+"\n\n"+p3+"\n\n"+p4+"\n\n"+p5+"\n\n"+p6+"\n\n"+p7+"\n\n"+p8+"\n\n"+p9)

def enviarStatus(v1, v2):  # RETORNA O TEXT COM INFORMAÇOES DE STATUS DE ACERTOS E ERROS
    global acertos
    global erros
    global banca

    t1 = float(v1)
    t2 = float(v2)
    t3 = t1 + t2
    t4 = "💥🟢 𝗦𝗜𝗡𝗔𝗟 𝗦𝗧𝗔𝗧𝗨𝗦 🟢💥"
    p2 = "🎯 𝗔𝗰𝗲𝗿𝘁𝗼𝘀 " + str(v1)
    p3 = "⛔️ 𝗘𝗿𝗿𝗼𝘀: " + str(v2)
    p4 = "📌 𝗥𝗼𝗱𝗮𝗱𝗮𝘀:" + str(t3)
    p5 = "⚠️ 𝗔𝗹𝗲𝗿𝘁𝗮: Entre até o 2x Martingale"
    p6 = "Dobre a aposta em cada Gale"
    p7 = "Ao ganhar espera o proximo sinal !!"
    p8 = "⚠️ Atenção: visite o meu website\n\nhttps://midsetpro.com.br/"
    enviarMenssagem(t4+"\n\n"+p2+"\n\n"+p3+"\n\n"+p4+"\n\n"+p5+"\n\n"+p6+"\n\n"+p7+"\n\n"+p8)



def win():
    global acertos
    global erros
    global analise_sinal
    global entrada
    global banca
    global cor_atual
    acertos += 1
    entrada = 0
    bot = telebot.TeleBot(token)
    bot.send_sticker(chat_id, 'CAACAgEAAxkBAAEHWbFjybxJtejWQ677CjHN8BaA8PoZngAC0QEAAo6ouERzvaHhBTM6eC0E')
    enviarStatus(acertos, erros)
    analise_sinal = False

def loss():
    global acertos
    global analise_sinal
    global erros
    erros += 1
    bot = telebot.TeleBot(token)
    bot.send_sticker(chat_id, 'CAACAgEAAxkBAAEHWbNjyb0F9kd2fPcTRtTMiASMywteDgACwwMAAkrvKERkva_EZ5ifFi0E')
    enviarStatus(acertos, erros)
    analise_sinal = False


def validate_gale():
    global entrada
    global expected
    global max_gale
    global cor_atual
    global banca
    entrada += 1
    if entrada <= max_gale:

        p1 = "🟢 GALE 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗢 🟢"
        p2 = "⚠️ atenção: "+ str(entrada) + " Martingale ⚠️" 
        p3 = "⚠️ entrar novamente no " + cor_atual
        p5 = "🐓2 martingale: (opcional)"
        p6 = "⚠️ 𝗔𝗹𝗲𝗿𝘁𝗮: Entre até o 2x Martingale"
        p7 = "Dobre a aposta em cada Gale"
        p8 = "Ao ganhar espera o proximo sinal !!"
        p9 = "⚠️ Atenção: visite o meu website\n\nhttps://midsetpro.com.br/"
        
        enviarMenssagem(p1+"\n\n"+p2+"\n\n"+p3+"\n\n"+p5+"\n\n"+p6+"\n\n"+p7+"\n\n"+p8+"\n\n"+p9)
    else:
        entrada = 0
        loss()

def validate_game(cor):
    if cor[0] == expected:
        win()
    elif cor[0] == 'B':
        win()
    else:
        validate_gale()

def analyze_game(cores):
    global analise_sinal
    global expected

    if cores[0] == 'V' and cores[2] == 'P' and cores[3] == 'V':
        analise_sinal = True
        expected = "V"
        print("Foi encontrada a sequencia esperimental  👻Ghost👻")
        enviar_sinal("🛑", "👻Ghost👻")
        
    elif cores[0] == 'P' and cores[2] == 'P':
        analise_sinal = True
        expected = "P"
        print("Foi encontrada a sequencia esperimental  👻Ghost👻")
        enviar_sinal("🛑", "👻Ghost👻")
    
    elif cores[0] == 'V' and cores[2] == 'V' and cores[3] == 'P':
        analise_sinal = True
        expected = "P"
        print("Foi encontrada a sequencia esperimental  👻Ghost👻")
        enviar_sinal("🛑", "👻Ghost👻")
        
    elif cores[0] == 'P' and cores[2] == 'V' and cores[3] == 'P':
        analise_sinal = True
        expected = "V"
        print("Foi encontrada a sequencia esperimental  👻Ghost👻")
        enviar_sinal("🛑", "👻Ghost👻")
        
    elif cores[2] == 'P' and cores[3]:
        analise_sinal = True
        expected = "V"
        print("Foi encontrada a sequencia esperimental  👻Ghost👻")
        enviar_sinal("🛑", "👻Ghost👻")
        
while True:
    url = "https://blaze.com/api/roulette_games/recent"
    req = requests.get(url)
    if req.status_code == 200:
        data = json.loads(req.content)
        jogo = [x['color'] for x in data]
        resultado = jogo
        conversor = {0: 'B', 1: 'V', 2: 'P'}
        resultado = [conversor[x] for x in resultado]
        if previous_data != resultado:
            print(resultado)
            if analise_sinal == True:
                validate_game(resultado)
            else:
                analyze_game(resultado)

            previous_data = resultado
    else:
        print("Erro ao obter dados da API")
    time.sleep(10)