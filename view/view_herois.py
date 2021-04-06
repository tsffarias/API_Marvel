from controller.controller_herois import Controller_herois

class View_herois:

    def __init__(self, flag='json'):
        self.controller = Controller_herois()
        self.flag = flag

    
    def linhas(self):
        print('='*100)

    
    def set_flag(self, flag):
        self.flag = flag

    def resposta_herois(self):
        resultado = self.controller.busca_herois(self.flag)    
        if resultado is not None and self.flag.lower() == 'json':
            self.linhas()
            self.mostra_dados_herois(resultado)
        
    def mostra_dados_herois(self, lista_herois):
        contador = 1
        for heroi in lista_herois:
            print(f'Heroi ({contador})')
            print(f'Nome heroi: {heroi.nome}')
            print(f'Descrição: {heroi.descricao}')
            print(f'Lista comics: {heroi.lista_comics}')
            print(f'Lista series: {heroi.lista_series}')
            self.linhas()
            contador += 1

        


	    

