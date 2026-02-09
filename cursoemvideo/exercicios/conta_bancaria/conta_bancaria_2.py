class ContaBancaria:
    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
            return f"ID: {self.id}, Titular: {self.titular}, Saldo: R${self.saldo:.2f}"
        
    def depositar(self, valor):
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")


c1 = ContaBancaria(123, "Felipe", 1000.0)
c1.depositar(500.0)
c1.sacar(200.0)
print(c1)