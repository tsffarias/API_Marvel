from controller.controller_herois import Controller_herois

class View_herois:

    def __init__(self, flag='json', qtd_herois=20):
        self.controller = Controller_herois()
        self.flag = flag
        self.qtd_herois = qtd_herois

    def linhas(self):
        print('▞▚'* 70)

    
    def espaco(self):
        print("")
    
    def set_flag(self, flag):
        self.flag = flag

    def resposta_herois(self):
        resultado = self.controller.busca_herois(self.flag, self.qtd_herois)    
        if resultado is not None and self.flag.lower() == 'json':
            self.linhas()
            self.mostra_dados_herois(resultado)
        elif resultado is not None and self.flag.lower() == 'csv':
            self.linhas()
            self.mostra_dados_herois(resultado)
        
    def mostra_dados_herois(self, lista_herois):
        contador = 1
        for heroi in lista_herois:
            self.espaco()
            print(f'❐ Heroi ({contador})')
            self.espaco()
            print(f'Nome heroi: {heroi.nome}')
            self.espaco()
            print(f'Descrição: {heroi.descricao}\n')
            self.espaco()

            print("Lista comics:")
            if len(heroi.lista_comics) == 0:
                print('No comics available')
            else:
                for comic in heroi.lista_comics:
                    print(comic)

            self.espaco()
            print("Lista series:")
            if len(heroi.lista_series) == 0:
                print('No series available')
            else:
                for serie in heroi.lista_series:
                    print(serie)

            self.espaco()
            self.linhas()
            contador += 1




	    

