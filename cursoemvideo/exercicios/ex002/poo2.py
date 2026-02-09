from time import sleep


class gafanhoto:
    '''
    Docstring for gafanhoto
    '''
    def __init__(self): #metodo construtor
        self.nome = str(input("Nome: "))
        self.idade = int(input("Idade: "))
        self.sexo = str(input("Sexo [M/F]: "))
        self.cidade = str(input("Cidade: "))

        print("--- Dados do Gafanhoto ---")

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e mora em {self.cidade}."
    
    def __getstate__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Cidade: {self.cidade}"

g1 = gafanhoto()


print(g1)
print(g1.__dict__) #atributos
print(g1.__getstate__())#metodo 
print(g1.__class__)
print(gafanhoto.__doc__)
