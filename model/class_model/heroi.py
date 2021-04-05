class Heroi:

    def __init__(self, nome, descricao):
        self.nome = nome
        self.lista_comics = list()
        self.lista_series = list()
        if descricao == '':
            self.descricao = 'No description available'
        else:
            self.descricao = descricao

    def set_lista_comics(self, comic):
        self.lista_comics.append(comic)
    
    def set_lista_series(self, serie):
        self.lista_series.append(serie)

    def __str__(self):
        return f'Nome: {self.nome}, Descricao: {self.descricao}, Lista Comics: {self.lista_comics}, Lista Series: {self.lista_series}'
