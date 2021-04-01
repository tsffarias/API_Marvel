from controller.controller_herois import Controller_herois

class View_herois:

    def __init__(self, flag='json'):
        self.controller = Controller_herois()
        self.flag = flag

    def set_flag(self, flag):
        self.flag = flag

    def resposta_herois(self):
        return self.controller.busca_herois(self.flag)




	    

