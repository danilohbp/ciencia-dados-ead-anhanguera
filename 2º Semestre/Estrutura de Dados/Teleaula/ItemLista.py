class ItemLista:
    """Representa cada item de uma lista encadeada"""
    def __init__(self, data=0, nexItem=None):
        self.data = data
        self.nextItem = nexItem
    
    def __repr__(self):
        return '%s => %s' % (self.data, self.nextItem)
        