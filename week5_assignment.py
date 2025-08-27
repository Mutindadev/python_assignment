# =============================================
# Assignment 1 & Activity 2 - Object-Oriented Programming in Python
# =============================================

# =======================
# Assignment 1: Design Your Own Class 🏗
# =======================

# Parent class
class Smartphone:
    def __init__(self, brand, model, price):
        # Attributes
        self.brand = brand
        self.model = model
        # Encapsulation -> private attribute
        self.__price = price  

    # Method to display smartphone details
    def phone_info(self):
        return f"{self.brand} {self.model} costs ${self.__price}"

    # Getter for price (encapsulation)
    def get_price(self):
        return self.__price

    # Setter for price (encapsulation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

# Child class (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        # Call parent constructor
        super().__init__(brand, model, price)
        self.gpu = gpu

    # Polymorphism -> override method
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.gpu} GPU is great for gaming!"

# Example usage
print("=== Assignment 1 Output ===")
phone1 = Smartphone("Samsung", "S23", 1000)
phone2 = GamingSmartphone("Asus", "ROG Phone 7", 1500, "Adreno 730")

print(phone1.phone_info())  
print(phone2.phone_info())  

phone1.set_price(1200)  # updating price
print(f"Updated Price: ${phone1.get_price()}")  


# =======================
# Activity 2: Polymorphism Challenge 🎭
# =======================

class Vehicle:
    def move(self):
        print("This vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")

# Example usage
print("\n=== Activity 2 Output ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each calls its own move() version (polymorphism in action!)