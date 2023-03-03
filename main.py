import csv


class Item:
    payRate = 0.8  # The payrate after giving a 20% Discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"The price: {price} here is (-)ve. Price has to be (+)ve"
        assert quantity >= 0, f"The quantity: {quantity} here is (-)ve. Quantity has to be (+)ve"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

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


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, brokenPhones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert brokenPhones >= 0, f"The Broken Pones: {brokenPhones} here is (-)ve. Quantity has to be (+)ve"

        # Assign to self object
        self.brokenPhones = brokenPhones


phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
print(Phone.all)
