nome = input('Digite seu nome: ')

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))

primeiro_nome = nome.split()[0]
print(len(primeiro_nome))