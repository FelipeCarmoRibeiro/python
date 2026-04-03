class funcionario:
    def __init__ (self,nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def __str__(self):
        return f"Funcionário: {self.nome}, Setor: {self.setor}, Cargo: {self.cargo}"
    

f1 = funcionario("Felipe", "TI", "Analista de Suporte")
print(f1)