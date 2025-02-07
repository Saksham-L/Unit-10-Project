class Batch:
    date = None
    grade = None
    quantity = None
    def __init__(self, date, grade, quantity):
        """
        Its a basic constructor, it just does whatever its supposed to do in Python
        """
        self.__date = date
        self.__grade = grade
        self.__quantity = quantity

    def display_details(self):
        """
        It's basically a __str__ thing but I want to have mine like this because it works better in my menu
        """
        return f"Date: {self.__date}, Grade: {self.__grade}, Quantity: {self.__quantity}"


class Inventory:
    batches = None
    warehouse_location = None
    manager = None
    def __init__(self, warehouse_location, manager):
        """
        Its a basic constructor, it just does whatever its supposed to do in Python
        """
        self.batches = []
        self.warehouse_location = warehouse_location
        self.manager = manager

    def add_batch(self, date, grade, quantity):
        """
        it will add a new batch to the list of batches in the inventory
        """
        self.batches.append(Batch(date, grade, quantity))

    def remove_batch(self, date, grade, quantity):
        """
        it will remove a batch from the list of batches in the inventory
        """
        self.batches = [batch for batch in self.batches 
                        if  (batch._Batch__date != date 
                             or batch._Batch__grade != grade 
                             or batch._Batch__quantity != quantity)
                             ]
    #I asked ai for a little help on how to syntax this weird thingy but I know how the code works

    def display_all_batches(self):
        """
        it will display all the batches in the inventory
        """
        return [batch.display_details() for batch in self.batches]


def menu():
    """
    Its the menu for the inventory tracker
    """
    warehouse_location = input("Enter warehouse location: ")
    manager = input("Enter manager name: ")
    inventory = Inventory(warehouse_location, manager)

    while True:
        print(f"\nWalter White's Inventory Tracker (FOR WHITE ROCK CANDY) - Managed by {inventory.manager}")
        print(f"Warehouse Location: {inventory.warehouse_location}")
        print("1. Add Batch")
        print("2. Remove Batch")
        print("3. View All Batches")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter batch date (YYYY-MM-DD): ")
            grade = input("Enter batch grade (1st grade, 2nd grade, 3rd grade): ")
            quantity = input("Enter batch quantity: ")
            inventory.add_batch(date, grade, quantity)
            print(f"Batch added: Date: {date}, Grade: {grade}, Quantity: {quantity}")

        elif choice == "2":
            date = input("Enter batch date to remove (YYYY-MM-DD): ")
            grade = input("Enter batch grade to remove: ")
            quantity = input("Enter batch quantity to remove: ")
            inventory.remove_batch(date, grade, quantity)
            print(f"Batch removed: Date: {date}, Grade: {grade}, Quantity: {quantity}")

        elif choice == "3":
            batches = inventory.display_all_batches()
            print("\nCurrent Inventory:")
            for batch in batches:
                print(batch)

        elif choice == "4":
            verification = input("are you sure? \n y/n: ")
            if verification == "y":
                print("Quiting")
                break
            elif verification == "n":
                inventory = Inventory(warehouse_location, manager)
        else:
            print("Error")


menu()



