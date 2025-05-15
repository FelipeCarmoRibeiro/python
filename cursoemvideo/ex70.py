
sex = str(input("Qual o seu sexo?[M/F]")).strip().upper()[0]
while sex not in "MF":
    sex = str(input("Dados invalidos, por favor informe seu sexo: ")).strip().upper*()[0]
    
print("Sexo {} registrado com sucesso".format(sex))