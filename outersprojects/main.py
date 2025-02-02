def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.2
    else:
        imposto = valor * 0.3

    return imposto

produto_1 = 2500
produto_2 = 1500
produto_3 = 500
imposto_produto1 = calcular_imposto(produto_1)
imposto_produto2 = calcular_imposto(produto_2)
imposto_produto3 = calcular_imposto(produto_3)
print(imposto_produto1)
print(imposto_produto2)
print(imposto_produto3)

    