class Heroi:

    def __init__(self, nome, descricao):
        self.nome = nome
        if descricao == '':
            self.descricao = 'No description available'
        else:
            self.descricao = descricao

    def __str__(self):
        return f'Nome: {self.nome}, Descricao: {self.descricao}'
