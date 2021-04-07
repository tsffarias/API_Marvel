import requests
import pandas as pd
import time
import hashlib
import yaml
import api_keys
from .class_model.heroi import Heroi

class Model_Herois():
    
    def __init__(self):
        self.url = 'http://gateway.marvel.com/v1/public/characters'


    def autenticacao_api_marvel(self):
        autentica = dict()

        timestamp = str(time.time())
        chave_publica = api_keys.public_key
        chave_privada = api_keys.private_key

        hash_string = timestamp + chave_privada + chave_publica
        hash_md5 = hashlib.md5(hash_string.encode()).hexdigest()

        autentica["timestamp"] = timestamp
        autentica["chave_publica"] = chave_publica
        autentica["chave_privada"] = chave_privada
        autentica["hash_md5"] = hash_md5

        return autentica

    def verificando_status_code(self, status):
        if status == 401:
            return [401, 'Status code: 401. O hash é inválido! ']
        else:
            return [200, 'Status Code: 200.  Tudo OK!']
        

    def requisicao_herois_marvel_json(self):
        dados_autenticacao = self.autenticacao_api_marvel()
        
        resposta = self.requisicao_api_marvel(dados_autenticacao)
        status = self.verificando_status_code(resposta.status_code)
        
        if status[0] == 200:
            print(status[1])
            return self.cria_lista_herois(resposta.json())
        else:
            print(status[1])

    
    def cria_lista_herois(self, json):
        lista_herois = list()
        
        for heroi in json['data']['results']:
            nome_heroi = heroi['name']
            descricao_heroi = heroi['description']

            heroi_dados = Heroi(nome_heroi, descricao_heroi)


            for lista_comics_heroi in heroi['comics']['items']:
                heroi_dados.set_lista_comics(lista_comics_heroi['name'])


            for lista_series_heroi in heroi['series']['items']:
                heroi_dados.set_lista_series(lista_series_heroi['name'])

            lista_herois.append(heroi_dados)

        return lista_herois


    def cria_herois_csv(self, csv):
        
        lista_herois = list()
        for heroi in csv:
            nome_heroi = heroi['name']
            descricao_heroi = heroi['description']
            heroi_dados = Heroi(nome_heroi, descricao_heroi)
            

            for lista_comics_heroi in heroi['comics']['items']:
                heroi_dados.set_lista_comics(lista_comics_heroi['name'])


            for lista_series_heroi in heroi['series']['items']:
                heroi_dados.set_lista_series(lista_series_heroi['name'])

            lista_herois.append(heroi_dados)
        
        return lista_herois
        
    
    def requisicao_herois_marvel_csv(self):
        dados_autenticacao = self.autenticacao_api_marvel()
        
        resposta = self.requisicao_api_marvel(dados_autenticacao)
        dado_csv = self.salva_csv(resposta.content)
        dado_csv = self.retorna_csv(dado_csv)
        return self.cria_herois_csv(dado_csv)
        
    def salva_csv(self, json):
        json = pd.read_json(json)
        dados_csv = json.to_csv(r'./marvel.csv', sep=',')
        return dados_csv

    def retorna_csv(self, dados_csv):
        dados_csv = pd.read_csv('marvel.csv', sep=',', usecols=['data'] )
        dados_csv = dados_csv.loc[3]
        dados_csv = dados_csv['data']
        dados_csv = yaml.safe_load(dados_csv)
        return dados_csv

    
    def requisicao_api_marvel(self, dados_autenticacao):
        return requests.get(f'{self.url}?ts={dados_autenticacao["timestamp"]}&apikey={dados_autenticacao["chave_publica"]}&hash={dados_autenticacao["hash_md5"]}')


