from art import *
from view.view_herois import View_herois


'''
Grupo: Michelle, Natalia, Thiago, Jenniffer, Felipe
Título: Projeto Módulo 2 - API Marvel
'''
def texto():
    print("O VamoAI é um projeto de formação de A N A L I S T A  D E  D A D O S, através de uma parceria do  I F O O D  com a instituição de ensino\n"
    "R E S I L I A. Ao final de cada módulo desenvolvemos um projeto. Para o fechamento do segundo módulo nós tivemos que desenvolver um soft-\n"
    "ware de requisição de API's, estruturado com o padrão MVC (Model-View-Controller). Em nosso algoritmo utilizamos o paradigma orientado a\n"
    "objetos e boas práticas de desenvolvimento de código, para a construção de um código limpo.\n")

    print("O Software recebe duas  F L A G S  e retorna os dados em dois formatos diferentes: J S O N  e  C S V. A API que escolhemos para trabalhar\n"
    "foi a disponibilizada pela Marvel. Nela, é possível obter dados sobre os heróis, as revistas em quadrinhos, os filmes e muito mais sobre\n"
    "o universo fantástico da  M A R V E L.")
    espaco()
    print('✓ Formatos disponíveis: \n'
    '• JSON → .json é um arquivo que contém uma série de dados estruturados a partir de chave e valor {Nome: José, Idade: 19}, em de formato\n'
    'texto e é utilizado para transferir informações entre sistemas. \n'
    '\n'
    '• CSV  → .csv armazena os dados separados por vírgulas em cada linha do arquivo. Neste formato os dados são apresentados em forma tabular.\n'
    'Exemplo:\n'
    'Nome, Matrícula, AV1, AV2 \n'
    'Andressa Marques, 01222019, 5.0, 6.5\n'
    'Bruno Farias, 01402019, 4.5, 5.2\n')

def espaco():
    print("")

def linhas():
    print('▞▚ '* 45)



if __name__ == '__main__':

    while (True):

        
        linhas()
        tprint("API: MARVEL".center(73))
        linhas()
        espaco()
        texto()
        espaco()

        resposta_usuario = input('❐ Digite a palavra referente ao formato escolhido (JSON ou CSV): ')
        padrao_resposta_formato = resposta_usuario.upper()
        if (padrao_resposta_formato != 'JSON') and (padrao_resposta_formato != 'CSV'):
            resposta_usuario = input("Opção inválida. Digite JSON ou CSV:")


        qtd_herois = int(input('❐ informe a quantidade de herois desejada (1 a 99): '))
        if qtd_herois >= 1 and qtd_herois <= 99:
            herois = View_herois(resposta_usuario, qtd_herois)
            resposta_qtd = herois.resposta_herois()
        else:
            print('Quantidade não suportada. Digite um número entre 1 e 100. ')
            print('Tente novamente.')


        espaco()
        resposta_nova_solicitacao = int(input('Digite (1), se desejar fazer uma nova consulta e (2) caso deseje finalizar:'))
        if resposta_nova_solicitacao == 2:
            print('Consulta finalizada!')
            break
        
            

    


