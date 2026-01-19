from abc import ABC, abstractmethod

# Component Interface
class FoodItem(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

# Concrete Components
class Pizza(FoodItem):
    def get_description(self) -> str:
        return "Pizza"

    def get_price(self) -> float:
        return 200.0

class Burger(FoodItem):
    def get_description(self) -> str:
        return "Burger"

    def get_price(self) -> float:
        return 100.0

# Decorator Base Class
class Decorator(FoodItem):
    def __init__(self, food_item: FoodItem):
        self.food_item = food_item

# Concrete Decorators
class ExtraCheeseDecorator(Decorator):
    def __init__(self, food_item: FoodItem, price: float):
        super().__init__(food_item)
        self.extra_cheese_price = price

    def get_description(self) -> str:
        return self.food_item.get_description() + " with Extra Cheese"

    def get_price(self) -> float:
        return self.food_item.get_price() + self.extra_cheese_price

class ExtraSauceDecorator(Decorator):
    def __init__(self, food_item: FoodItem, price: float):
        super().__init__(food_item)
        self.extra_sauce_price = price

    def get_description(self) -> str:
        return self.food_item.get_description() + " with Extra Sauce"

    def get_price(self) -> float:
        return self.food_item.get_price() + self.extra_sauce_price

class ExtraToppingsDecorator(Decorator):
    def __init__(self, food_item: FoodItem, price: float):
        super().__init__(food_item)
        self.extra_toppings_price = price

    def get_description(self) -> str:
        return self.food_item.get_description() + " with Extra Toppings"

    def get_price(self) -> float:
        return self.food_item.get_price() + self.extra_toppings_price

# Client code
if __name__ == "__main__":

    pizza_order: FoodItem = Pizza()
    burger_order: FoodItem = Burger()

    pizza_order = ExtraCheeseDecorator(pizza_order, 10.0)
    pizza_order = ExtraSauceDecorator(pizza_order, 5.0)

    burger_order = ExtraCheeseDecorator(burger_order, 20.0)
    burger_order = ExtraToppingsDecorator(burger_order, 15.0)

    print("Description of pizza order is:", pizza_order.get_description())
    print("Price of pizza order is:", pizza_order.get_price())

    print("Description of burger order is:", burger_order.get_description())
    print("Price of burger order is:", burger_order.get_price())
