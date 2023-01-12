from anytree import Node, NodeMixin
from day07.fyle import Fyle

class Dir(NodeMixin):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def append_subdir(self, name_or_subdir):
        if isinstance(name_or_subdir, Dir):
            name_or_subdir.parent = self
            return

        name = name_or_subdir
        if not [d for d in self.children if d.name == name]:
            Dir(name, parent=self)

    def append_file(self, f):
        f.parent = self

    def sum_size(self):
        child_sizes = sum([d.sum_size() for d in self.children if isinstance(d, Dir)])
        file_sizes = sum([f.size for f in self.children if isinstance(f, Fyle)])
        return child_sizes + file_sizes

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
