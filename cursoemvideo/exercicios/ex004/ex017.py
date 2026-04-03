from rich.panel import Panel

class Produto():
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        conteudo = f"{self.nome}"
        valor = f"{self.preço}"
        etiqueta = Panel(conteudo)
        return etiqueta

p1 = Produto("Iphone 17 Pro Max", "12.000")
p2 = Produto("Computador Gamer", "8.000")

print(p1.etiqueta())
