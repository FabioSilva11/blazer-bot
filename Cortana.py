#robo da blazer fabio silva

from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://blaze.com/pt/games/double')

lista = navegador.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

list = lista.split()

sequencia = list[0:6]

print(sequencia)

cor = '-'
send_message = '-'

if "1" in sequencia:
   #Vermelho
   cor = cor +  'Vermelho-'
   
         
if "2" in sequencia:

   #Vermelho
   cor = cor +  'Vermelho-'
   
if "3" in sequencia:

   #Vermelho
   cor = cor +  'Vermelho-'

if "4" in sequencia:

   #Vermelho
   cor = cor +  'Vermelho-'
   
if "5" in sequencia:

   #Vermelho
   cor = cor +  'Vermelho-'
   
if "6" in sequencia:

   #Vermelho
   cor = cor +  'Vermelho-'
   
if "7" in sequencia:

   #Vermelho
   cor = cor +  'Vermelho-'
    
if "8" in sequencia:

   #Preto
   cor = cor +  'Preto-'
    
if "9" in sequencia:

   #Preto
   cor = cor +  'Preto-'

if "10" in sequencia:

   #Preto
   cor = cor +  'Preto-'

if "11" in sequencia:

   #Preto
   cor = cor +  'Preto-'
    
if "12" in sequencia:

   #Preto
   cor = cor +  'Preto-'
   
if "13" in sequencia:

   #Preto
   cor = cor +  'Preto-'
   
if "14" in sequencia:

   #Preto
    cor = cor +  'Preto-'

print('['+cor+']')

if cor == '-Vermelho-Vermelho-Vermelho-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Vermelho-Vermelho-Preto-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
               
if cor == '-Preto-Preto-Vermelho-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Vermelho-Preto-Vermelho-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Preto-Vermelho-Preto-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Preto-Preto-Preto-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Vermelho-Vermelho-Vermelho-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Vermelho-Preto-Preto-Preto':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Preto-Vermelho-Vermelho-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Preto-Preto-Vermelho-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Preto-Vermelho-Vermelho-Preto ':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Vermelho-Preto-Preto-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Preto-Vermelho-Preto-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'

if cor == '-Preto-Preto-Vermelho-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! 🔴  Vermelho!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'
                
if cor == '-Vermelho-Vermelho-Preto-Vermelho-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'

if cor == '-Vermelho-Preto-Preto-Preto-':
            send_message = '
                🔔⚠️🚨Atenção🚨⚠️🔔
                ✅Entrada confirmada! ⚫  Preto!
                ✅Ate Gale 2 🐓🐓 
                🎲Jogue agora Blaze Double🎲  
                (https://blaze.com/r/LnX9VB)
                💬 por: t.me/xX1chatbot 🥷🏾'


print(send_message)
