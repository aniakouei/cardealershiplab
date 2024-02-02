#create the vehicle class
    #initialize self, make, miles and price
    #create function for starting engine
    #create function to make noise
#create an inherited class called Truck that inherits Vehicle
    #initialize and create function to load cargo
#create an inherited class called Motorcycle that inherits Vehicle
    #create a make noise function
#create a function to display the vehicle list and to list it 1,2,3...
#create another funtion names main to put all the main code inside
    #print hello statement
    #print lists with information for motorcycles and trucks
    #create an empty list
    #create a loop for user input for b or t
        #if statement for each choice
    #statement to compare vehicles
        #if statement based on if they choose yes or no
        #print statement and als print the noise the vehicle makes
#call main to run program



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
