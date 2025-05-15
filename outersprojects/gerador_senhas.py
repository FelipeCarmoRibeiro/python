import random


print("Gerador de senhas")

numeros = ['1','2','3','4','5']
letras = ['a', 'b','c','d','e']

def gerar_senha(tamanho= 10):
    caracteres = numeros + letras
    senha = "".join(random.choices(caracteres, k=tamanho))
    return senha

print("Sua senha é:", gerar_senha())