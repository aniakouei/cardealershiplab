class Vehicle:
    def __init__(self, make, miles, price):
        self.make=make
        self.miles=miles
        self.price=price
        self.engineon=False

    def start_engine(self):
        print("Starting engine...")
        self.engineon=True

    def make_noise(self):
        print("Beep Beep!")

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargoproperty=False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargoproperty=True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed=top_speed

    def make_noise(self):
        print("Vroom vroom!")

def display(vehicle_list):
    for i, vehicle in enumerate(vehicle_list, start=1):
        print(f"{i}. {vehicle.make}: with {vehicle.miles} miles costs ${vehicle.price}")

def main():
    print("Hello")
    print("Welcome to GC Bikes and Trucks!")

    bikes = [
       Motorcycle("Harley", 0, 50000,200),
        Motorcycle("Ducati", 1000, 50000, 150),
        Motorcycle("Honda", 20000, 50000, 100)
    ]

    trucks = [
        Truck("Toyota", 10000, 30000),
        Truck("Ford", 20000, 5000),
        Truck("Chevy", 50000, 20000)
    ]

    vehicles_to_compare = []

    while True:
        choice = input("Would you like to view bikes or trucks? (b or t)").lower()

        if choice == "b":
            print("Bikes:")
            display(bikes)
            compare_choice = input("Would you like to compare one of these vehicles today? (y or n) ").lower()
            if compare_choice == "y":
                selection = int(input("Which vehicle would you like to compare? (Please list number) ")) - 1
                vehicles_to_compare.append(bikes[selection])
                print(f"{bikes[selection].make} added!")

        elif choice == "t":
            print("Trucks:")
            display(trucks)
            compare_choice = input("Would you like to compare one of these vehicles today? (y or n) ").lower()
            if compare_choice == "y":
                selection = int(input("Which vehicle would you like to compare? (Please list number) ")) - 1
                vehicles_to_compare.append(trucks[selection])
                print(f"{trucks[selection].make} added!")

        else:
            print("Invalid choice. Please enter 'b' or 't'.")

        compare_now = input("Would you like to compare your vehicles now? (y or n) ").lower()
        if compare_now == "y":
            print("Here are your vehicles to compare:")
            for vehicle in vehicles_to_compare:
                print(f"{vehicle.make}: with {vehicle.miles} miles costs ${vehicle.price}")
                vehicle.make_noise()

            print("Thank you and have a nice day!")
            break

main()
