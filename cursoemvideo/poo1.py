from time import sleep


class gafanhoto:
    def __init__(self): #metodo construtor
        self.nome = str(input("Nome: "))
        self.idade = int(input("Idade: "))
        self.sexo = str(input("Sexo [M/F]: "))
        self.cidade = str(input("Cidade: "))

    print("--- Dados do Gafanhoto ---")

    def apresentar(self):
        print("--- Apresentação ---")
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo}\nCidade: {self.cidade}")


    def mensagem(self):
        sleep(3)
        return f"{self.nome} tem {self.idade} anos e mora em {self.cidade}."

g1 = gafanhoto()
g1.apresentar()
g1.mensagem()