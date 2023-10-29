class Dados:
    """Permite a criação de uma estrutura para gravar dados"""
    def __init__(self):
        self.itens = []
    
    def __repr__(self):
        return str(self.itens)

    def insere(self, valor):
        """Adiciona itens à sua lista de dados"""
        self.itens.append(valor)

    def remove(self):
        # Modifica o valor do último item
        self.itens.pop()

def main():
    # Cria um novo objeto do tipo Dados
    dados = Dados()

    # Adicionando itens
    dados.insere(1)
    dados.insere(2)
    dados.insere(3)

    print(dados)

    # Removendo itens
    dados.remove()

    print(dados)

if __name__ == "__main__":
    main()

