class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"The price: {price} here is (-)ve. Price has to be (+)ve"
        assert quantity >= 0, f"The quantity: {quantity} here is (-)ve. Quantity has to be (+)ve"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, -5)
item2 = Item("Laptop", 1000, 3)


print(item1.name, item1.price, item1.quantity)
print(item1.calculateTotalPrice())

print(item2.name, item2.price, item2.quantity)
print(item2.calculateTotalPrice())
