from day3.compartment import Compartment
from day3.item import Item

def test_as_str():
    c = Compartment("aBc")
    assert c.as_str() == "aBc"

def test_has_item():
    c = Compartment("aBc")
    assert c.has_item(Item("B")) == True
