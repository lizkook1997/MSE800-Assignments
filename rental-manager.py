# class RentalManager:
#     _instance = None
 
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(RentalManager, cls).__new__(cls)
#             cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
#         return cls._instance
 
#     def rent_car(self, car_name):
#         if car_name in self.cars_available:
#             self.cars_available.remove(car_name)
#             print(f"{car_name} has been rented.")
#         else:
#             print(f"{car_name} is not available.")
 
#     def show_available_cars(self):
#         print("Available cars:", self.cars_available)
 
 
# manager1 = RentalManager()
# manager2 = RentalManager()
 
# manager1.rent_car("Honda")
# manager2.show_available_cars()  # Affects both because it's the same instance
 
# print("Address of manager1:", id(manager1))
# print("Address of manager2:", id(manager2))

# print("Are both managers the same object?", manager1 is manager2)         
# 
# 
# Is "car_name" variable is the same location in the memory? Debug the code to get the name of the car from end user? See below code:
 
 
 
class RentalManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance

    def rent_car(self, car_name):
        print(f"[DEBUG] Memory address of input car_name: {id(car_name)}")
        for car in self.cars_available:
            print(f"[DEBUG] Comparing with car in list: {car} (id: {id(car)})")
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
        else:
            print(f"{car_name} is not available.")

    def show_available_cars(self):
        print("Available cars:", self.cars_available)


# Get car name from user
car_name = input("Enter the car you want to rent: ").strip()

manager1 = RentalManager()
manager2 = RentalManager()

manager1.rent_car(car_name)
manager2.show_available_cars()

print("Are both managers the same object?", manager1 is manager2)
