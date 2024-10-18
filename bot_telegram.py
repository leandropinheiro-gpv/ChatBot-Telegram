# -*- coding: utf-8 -*-
import json
import requests

#############################################################################
#Classe telegram
class TelegramBot:
        
    def __init__(self, token):
        self.token = token
        self.config = {'url': 
          'https://api.telegram.org/bot' +
          token + '/'}
    
    def pegar_novas_mensagens(self):
        x = ''
        try:
            x = json.loads(requests.get(self.config['url'] + 'getUpdates').text)
        except Exception as e:
            x = ''
            if 'Failed to establish a new connection' in str(e):
                print('Perca de conexao telegram')
            else:
                print('Erro desconhecido no telegram: ' + str(e))
        return x
    
    def del_update(self, data):
    	    	
    	#self.config['lock'].acquire()
    	requests.post(self.config['url'] + 'getUpdates', {'offset': data['update_id']+1})
    	#self.config['lock'].release()
    
    def send_message(self, data, msg):
    	
    	#self.config['lock'].acquire()
    	requests.post(self.config['url'] + 'sendMessage', {'chat_id': data['message']['chat']['id'], 'text': str(msg)})
    	#self.config['lock'].release()
        
    
