from rich import print
from rich import inspect

class Funcionario():
    __doc__ = "Funcionario"

    empresa = "Grupo Le Lac"

    def __init__(self, nome, setor, cargo):
        self.nome = str(nome)
        self.setor = str(setor)
        self.cargo = str(cargo)
    
    def apresentacao(self):
        return f"Olá sou {self.nome}, fico no setor da {self.setor}, e sou {self.cargo}, trabalho na empresa {Funcionario.empresa}"



c1 = Funcionario("Felipe", "TI", "Aprendiz")
c2 = Funcionario("Vinicius", "TI", "Junior")


inspect(c1, methods=True)
inspect(c2, methods=True)
print(c1.apresentacao())
print(c2.apresentacao())
        