from rich import inspect


class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f'{inspect.nome} - R${inspect.preco:.2f}'
    


p1 = produto("Camiseta", 49.90)
p1.etiqueta()

