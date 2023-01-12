from anytree import NodeMixin

class Fyle(NodeMixin):
    def __init__(self, name : str = None, size : int = None, parent = None):
        self.name = name
        self.size = size
        self.parent = parent

    def __repr__(self):
        return f'{self.name} (file, size={self.size})'
