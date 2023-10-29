class Pilha:
    """Permite a criação de uma pilha"""
    def __init__(self):
        self.itens = []
    
    def __repr__(self):
        return str(self.itens)

    def empilha(self, valor):
        """Adiciona itens à pilha"""
        self.itens.append(valor)
    
    def desempilha(self):
        assert self.itens, "Erro: pilha vazia."
        # Modifica o valor do topo
        return self.itens.pop()

# Cria um novo objeto do tipo Pilha
pilha = Pilha()

# Adiciona um item à Pilha
pilha.empilha(1)
pilha.empilha(2)
pilha.empilha(3)
pilha.empilha(4)
pilha.empilha(5)
print(pilha)

# Remove o item da pilha
pilha.desempilha()
print(pilha)