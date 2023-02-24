
class Pizza:
    def __init__(self, toppings: list):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping)-> bool:
        return topping != 'pineapple'

ingredients = ['cheese', 'onions'] # spam is not a topping

if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    print(pizza.toppings)
else:
    print('No pineapples!')