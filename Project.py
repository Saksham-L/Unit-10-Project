import csv

class Shipment:
    def __init__(self, date, product_name, quantity):
        """
        Its a basic constructor, it just does whatever its supposed to do in Python
        """
        self.__date = date
        self.__product_name = product_name
        self.__quantity = quantity

    def display_details(self):
        """
        It's basically a __str__ thing but I want to have mine like this because it works better in my menu
        """
        return f"Date: {self.__date}, Product Name: {self.__product_name}, Quantity: {self.__quantity}"

    def to_csv_row(self):
        """
        Convert shipment details to a list suitable for CSV writing
        """
        return [self.__date, self.__product_name, self.__quantity]


class Inventory:
    def __init__(self, warehouse_location, manager):
        """
        Its a basic constructor, it just does whatever its supposed to do in Python
        """
        self.shipments = []
        self.warehouse_location = warehouse_location
        self.manager = manager
        self.filename = f'{warehouse_location}_inventory.csv'
        self.manager_file = f'{warehouse_location}_manager_log.txt'

        
        self.save_manager_info()

    def save_manager_info(self):
        """
        Save the manager name and warehouse info to a text file
        """
        with open(self.manager_file, mode='a') as file:
            file.write(f"Manager: {self.manager}\n")

    def log_user_action(self, user_name, action):
        """
        Log user actions (like adding or removing shipments)
        """
        with open(self.manager_file, mode='a') as file:
            file.write(f"{user_name} performed action: {action}\n")

    def add_shipment(self, date, product_name, quantity, user_name):
        """
        it will add a new shipment to the list of shipments in the inventory
        """
        self.shipments.append(Shipment(date, product_name, quantity))
        self.log_user_action(user_name, f"Added shipment - Date: {date}, Product: {product_name}, Quantity: {quantity}")
        self.save_to_csv()

    def remove_shipment(self, date, product_name, quantity, user_name):
        """
        it will remove a shipment from the list of shipments in the inventory
        """
        self.shipments = [shipment for shipment in self.shipments 
                           if (shipment._Shipment__date != date 
                               or shipment._Shipment__product_name != product_name 
                               or shipment._Shipment__quantity != quantity)]
        self.log_user_action(user_name, f"Removed shipment - Date: {date}, Product: {product_name}, Quantity: {quantity}")
        self.save_to_csv()

    def display_all_shipments(self):
        """
        it will display all the shipments in the inventory
        """
        return [shipment.display_details() for shipment in self.shipments]

    def save_to_csv(self):
        """
        Save all shipments to a CSV file
        """
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Product Name", "Quantity"])
            for shipment in self.shipments:
                writer.writerow(shipment.to_csv_row())

    def load_from_csv(self):
        """
        Load shipments from a CSV file
        """
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.shipments.append(Shipment(row["Date"], row["Product Name"], row["Quantity"]))
        except FileNotFoundError:
            print(f"No previous data found for warehouse '{self.warehouse_location}'.")


def menu():
    """
    Its the menu for the inventory tracker
    """
    warehouse_location = input("Enter warehouse location: ")
    manager = input("Enter manager name: ")
    inventory = Inventory(warehouse_location, manager)
    
    
    inventory.load_from_csv()

    while True:
        print(f"\nWarehouse Inventory Tracker - Managed by {inventory.manager}")
        print(f"Warehouse Location: {inventory.warehouse_location}")
        print("1. Add Shipment")
        print("2. Remove Shipment")
        print("3. View All Shipments")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter your name: ")
            date = input("Enter shipment date (YYYY-MM-DD): ")
            product_name = input("Enter product name: ")
            quantity = input("Enter shipment quantity: ")
            inventory.add_shipment(date, product_name, quantity, user_name)
            print(f"Shipment added: Date: {date}, Product Name: {product_name}, Quantity: {quantity}")

        elif choice == "2":
            user_name = input("Enter your name: ")
            date = input("Enter shipment date to remove (YYYY-MM-DD): ")
            product_name = input("Enter product name to remove: ")
            quantity = input("Enter shipment quantity to remove: ")
            inventory.remove_shipment(date, product_name, quantity, user_name)
            print(f"Shipment removed: Date: {date}, Product Name: {product_name}, Quantity: {quantity}")

        elif choice == "3":
            shipments = inventory.display_all_shipments()
            print("\nCurrent Inventory:")
            for shipment in shipments:
                print(shipment)

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Error")


menu()
