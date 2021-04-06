from art import *
from view.view_herois import View_herois

'''
Grupo: Michelle, Natalia, Thiago, Jenniffer, Felipe
Título: Projeto Módulo 2 - API Marvel
'''

def linhas():
    print('='*100)

if __name__ == '__main__':
    
    linhas()
    tprint("API: MARVEL".center(40))
    linhas()
    resposta_usuario = input('Qual formato de dado você quer? (JSON ou CSV): ')

    herois = View_herois(resposta_usuario)
    herois.resposta_herois()

    


