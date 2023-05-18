class Carteira:
    saldo = 0
    
    def adicionar_fundos(self, valor):
        self.saldo += valor
        print('Operação realizada com sucesso')
    
    def remover_fundos(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Operação concluída')
        else:
            print('Operação não realizada. Saldo insuficiente')

c = Carteira()
print(f"Saldo: R$ {c.saldo:.2f}", end="\n\n")
print("== Adicionar fundos ==")
c.adicionar_fundos(50)
print()
print(f"Saldo: R$ {c.saldo:.2f}", end="\n\n")
print("== Remover fundos ==")
c.remover_fundos(30)
print()
print(f"Saldo: R$ {c.saldo:.2f}", end="\n\n")
