class Item:
    payRate = 0.8  # The payrate after giving a 20% Discount

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

    def applyDiscount(self):
        self.price = self.price * self.payRate


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
