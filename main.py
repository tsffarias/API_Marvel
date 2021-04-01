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

    resposta_usuario = input('Qual formato de dado você quer? (JSON ou CSV): ')

    herois = View_herois(resposta_usuario)
    resposta = herois.resposta_herois()

    if resposta_usuario.lower() == 'json':
        linhas()
        mostra_dados_herois(resposta)


