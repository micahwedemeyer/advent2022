from day3.item import Item

class Compartment:
    def __init__(self, item_str):
        self.items = list(map(Item, item_str))

    def has_item(self, item):
        return item.char() in self.as_str()

    def as_str(self):
        return "".join(map(lambda i: i.char(), self.items))

    def as_set(self):
        return set(self.items)
