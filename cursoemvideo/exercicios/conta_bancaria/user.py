from app import conta_bancaria


print("=== Conta Bancária ===")

def encontrar_conta(conta,id_procurada):
    if conta.id == id_procurada:
        print(f"Conta encontrada: {conta.titular}, Saldo: R${conta.saldo:.2f}")
    else:
        print("Conta não encontrada.")

conta1 = conta_bancaria(123, "Felipe", 1000.0)

id_digitada = int(input("Digite o ID da conta para procurar: "))
encontrar_conta(conta1, id_digitada)

