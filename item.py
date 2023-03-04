import csv


class Item:
    payRate = 0.8  # The payrate after giving a 20% Discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"The price: {price} here is (-)ve. Price has to be (+)ve"
        assert quantity >= 0, f"The quantity: {quantity} here is (-)ve. Quantity has to be (+)ve"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Arrtibute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The length of the name is too long!")
        else:
            self.__name = value

    def calculateTotalPrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.payRate

    @classmethod
    def instantiateFromCSV(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def isInteger(num):
        # We will count out the Floats that are point Zero
        # For i.e. 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point Zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
