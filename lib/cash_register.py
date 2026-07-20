#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        
        if type(discount) == int and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) == int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        item_total = price * quantity
        self.total += item_total

        new_items = [item] * quantity

        for single_item in new_items:
            self.items.append(single_item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "item_total": item_total
        }
        self.previous_transactions.append(transaction)
        return f"Added {quantity} x {item} at ${price} each."

    def apply_discount(self):
        if self._discount > 0:
            discount_amount = self.total * (self._discount / 100)
            self.total -= discount_amount
            return f"Applied {self._discount}% discount. New total is ${self.total}"
        return "There is no discount to apply."

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return "There is no transaction to void."

        last_transaction = self.previous_transactions.pop()

        self.total -= last_transaction["item_total"]

        items_to_remove = [last_transaction["item"]] * last_transaction["quantity"]

        for item in items_to_remove:
            if item in self.items:
                self.items.remove(item)

        return f"Voided last transaction: {last_transaction['item']}"


register = CashRegister(20)

# Add items
print(register.add_item("Apple", 2, 3))  
print(register.add_item("Milk", 4, 1))   

print("Cart Items:", register.items)
print("Total Price:", register.total)

print(register.void_last_transaction())
print("Items after void:", register.items)
print("Total after void:", register.total)