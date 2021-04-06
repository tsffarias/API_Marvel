import requests
import pandas as pd
import time
import hashlib
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
        if status == 409:
            return [409, 'Status Code 409. Parametros de chave de validação ausente!.']
        elif status == 401:
            return [401, 'Status code: 401. Parametros(ts, hash, apikey) enviados estão invalidos!']
        elif status == 405:
            return [405, 'Status code: 405. Verbo HTTP não permitido!']
        elif status == 403:
            return [403, 'Status code: 403. Você não tem acesso a este terminal.']
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

            # extraindo dados comics
            for lista_comics_heroi in heroi['comics']['items']:
                heroi_dados.set_lista_comics(lista_comics_heroi['name'])

            # extraindo dados series
            for lista_series_heroi in heroi['series']['items']:
                heroi_dados.set_lista_series(lista_series_heroi['name'])

            lista_herois.append(heroi_dados)

        return lista_herois
        

    def requisicao_herois_marvel_csv(self):
        dados_autenticacao = self.autenticacao_api_marvel()

        resposta = self.requisicao_api_marvel(dados_autenticacao)
        dado_csv = self.converte_em_csv(resposta.content)
        print(dado_csv)
        #return dado_csv
        
    
    def converte_em_csv(self, json):
        dados = pd.read_json(json)
        return dados.to_csv()

    
    def requisicao_api_marvel(self, dados_autenticacao):
        return requests.get(f'{self.url}?ts={dados_autenticacao["timestamp"]}&apikey={dados_autenticacao["chave_publica"]}&hash={dados_autenticacao["hash_md5"]}')


