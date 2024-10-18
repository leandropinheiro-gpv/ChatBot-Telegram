# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from time import sleep
from decouple import config
import bot_telegram


TOKEN = config('TOKEN')

##############################################################################
#Bot Telegram
def mensagens_telegram():
   ##########################################################################
   #iniciando o chatbot
   chatbot = ChatBot('Meu Bot',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
            statement_comparison_function = LevenshteinDistance)
   ##########################################################################
   #iniciando as funçoes do telegram

   telegrambot = bot_telegram.TelegramBot(TOKEN)
   msgtelegram = telegrambot.pegar_novas_mensagens()
   if len(msgtelegram['result']) > 0:
        for data in msgtelegram['result']:
            telegrambot.del_update(data)
            #print(json.dumps(data, indent=1))
            pergunta = data['message']['text']
            response = chatbot.get_response(pergunta)	
            telegrambot.send_message(data, response)

##############################################################################
#loop principal do chatbot
while True:
    mensagens_telegram()
    	
    sleep(0.2)
    
    
    
