class Item:
    ORD_LOWER_OFFSET = 97
    ORD_UPPER_OFFSET = 65

    LOWER_START = 1
    UPPER_START = 27

    def __init__(self, item_char):
        self.item_char = item_char

    def char(self):
        return self.item_char

    def priority(self):
        ord_code = ord(self.item_char)
        if (self.item_char.isupper()):
            return ord_code - self.ORD_UPPER_OFFSET + self.UPPER_START
        else:
            return ord_code - self.ORD_LOWER_OFFSET + self.LOWER_START

    def __hash__(self):
        return hash(self.item_char)

    def __eq__(self, other):
        return isinstance(other, Item) and self.char() == other.char()
