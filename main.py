from art import *
from view.view_herois import View_herois

'''
Grupo: Michelle, Natalia, Thiago, Jenniffer, Felipe
Título: Projeto Módulo 2 - API Marvel
'''

def linhas():
    print('='*100)

def mostra_dados_herois(lista_herois):
    contador = 1
    for heroi in lista_herois:
        print(f'Heroi ({contador})')
        print(f'Nome heroi: {heroi.nome}')
        print(f'Descrição: {heroi.descricao}')
        linhas()
        contador += 1

if __name__ == '__main__':
    
    linhas()
    tprint("API: MARVEL".center(40))
    linhas()

    flag = 'json'

    herois = View_herois(flag)
    resposta = herois.resposta_herois()

    if flag == 'json':
        mostra_dados_herois(resposta)


