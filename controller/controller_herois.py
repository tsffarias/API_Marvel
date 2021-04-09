from model.model_herois import Model_Herois

class Controller_herois:
    
    def __init__(self):
        self.model = Model_Herois()


    def busca_herois(self, flag, qtd_herois):
        if flag.lower() == 'json':
            return self.requisicao_herois_json(qtd_herois)
        elif flag.lower() == 'csv':
            return self.requisicao_herois_csv(qtd_herois)
        else:
            print('Formato inválido')

    def requisicao_herois_json(self, qtd_herois):
        resultado = self.model.requisicao_herois_marvel_json(qtd_herois)
        return resultado

    def requisicao_herois_csv(self, qtd_herois):
        resultado = self.model.requisicao_herois_marvel_csv(qtd_herois)
        return resultado



