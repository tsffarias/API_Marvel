from model.model_herois import Model_Herois

class Controller_herois:
    
    def __init__(self):
        self.model = Model_Herois()

    def validacao_flag(self, flag):
        if flag.lower() == 'json' or flag.lower() == 'csv':
            return True
        else:
            return False

    def busca_herois(self, flag):
        if self.validacao_flag(flag):
            if flag.lower() == 'json':
                return self.requisicao_herois_json()
            else:
                return self.requisicao_herois_csv()
        else:
            print('Flag inválida')

    def requisicao_herois_json(self):
        resultado = self.model.requisicao_herois_marvel_json()
        return resultado

    def requisicao_herois_csv(self):
        resultado = self.model.requisicao_herois_marvel_csv()
        return resultado



