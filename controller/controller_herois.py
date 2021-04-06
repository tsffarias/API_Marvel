from model.model_herois import Model_Herois

class Controller_herois:
    
    def __init__(self):
        self.model = Model_Herois()


    def busca_herois(self, flag):
        if flag.lower() == 'json':
            return self.requisicao_herois_json()
        elif flag.lower() == 'csv':
            return self.requisicao_herois_csv()
        else:
            print('Formato inválido')

    def requisicao_herois_json(self):
        resultado = self.model.requisicao_herois_marvel_json()
        return resultado

    def requisicao_herois_csv(self):
        resultado = self.model.requisicao_herois_marvel_csv()
        return resultado



