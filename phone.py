from item import Item


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
