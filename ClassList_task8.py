class Shop(object):
    open = False

    def __init__(self, shop_name, store_type=None, number_of_units=0):
        if store_type is None:
            store_type = []

        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"Магазин {self.shop_name} продає {self.store_type}")

    def open_shop(self):
        self.open = True

    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units
        return self.number_of_units

    def increment_number_of_units(self, number_of_units):
        self.number_of_units += number_of_units
        return self.number_of_units


class Discount(Shop):
    def __init__(self, shop_name, discount_products=None):
        if discount_products is None:
            discount_products = []

        super().__init__(shop_name)
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        print(f"Товари зі знижкою => {self.discount_products}")
