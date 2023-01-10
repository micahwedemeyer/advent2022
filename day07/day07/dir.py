from anytree import Node, NodeMixin

class Dir(NodeMixin):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def append_subdir(self, name):
        if not [d for d in self.children if d.name == name]:
            Dir(name, parent=self)

    def append_file(self, f):
        f.parent = self
