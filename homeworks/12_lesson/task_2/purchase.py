class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        customer = f"User: {self.user}\n"
        items = ""
        for item in self.products:
            items += f"{item.name}: {self.products.get(item)} pcs.\n"
        return f"{customer}Items:\n{items}"

    def get_total(self):
        total_price = 0
        for item in self.products:
            total_price += self.products.get(item) * item.price
        return total_price
