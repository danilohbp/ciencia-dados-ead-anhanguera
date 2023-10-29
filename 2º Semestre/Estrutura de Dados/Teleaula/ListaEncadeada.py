import ItemLista as il

class ListaEncadeada:

    def __init__(self):
        self.head = None
        self.lista = []

    def __repr__(self):
        return "%s" % (self.head)
    
    def insere(self, lista, data):
        # Cria um objeto para armazenar um novo item da lista
        item = il.ItemLista(data)

        # O head é apontado como próximo Item
        item.nextItem = lista.head

        # O item atual se torna o head
        lista.head = item
    
    def busca(self, lista, valor):
        navegar = lista.head
        while navegar and navegar.data != valor:
            navegar = navegar.nextItem
        return navegar
    
    def remove(self, valor):
        # Verificamos se o item se trata do head
        if self.head.data == valor:
            self.head = self.head.nextItem
        else:
            # Detectando a posição do elemento
            before = None
            navegar = self.head

            # Navega pelo cabeçalho atual
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.nextItem

            # Remove o item atual
            if navegar:
                before.nextItem = navegar.nextItem
            else:
                before.nextItem = None


if __name__ == '__main__':
    lista = ListaEncadeada()
    lista.insere(lista, "Abacaxi")
    lista.insere(lista, "Tomate")
    lista.insere(lista, "Melancia")
    lista.insere(lista, "Laranja")

    print("Conteúdo da lista: ", lista)

    print(lista.busca(lista, "Abacaxi"))
    lista.remove("Abacaxi")