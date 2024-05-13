import random
class Product:
    def __init__(self, supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year):
        self.supermarket_name = supermarket_name
        self.__product_ID = product_ID
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def add_new_product(self):
        self.name = input('Enter the name of the new product: ')
        self.price = float(input('Enter the price of the new product: '))
        self.manufacturer = input('Enter the manufacturer of the new product: ')
        self.weight = float(input('Enter the weight of the new product: '))
        self.expiration_date = input('Enter the expiration date of the new product: ')
        self.year = input('Enter the year of the new product: ')
        self.__product_ID = random.randint(10000, 1000000)
        print('Product added successfully.')

    def change_productID(self):
        new_product_ID = input('Enter the new product ID: ')
        self.__product_ID = new_product_ID
        print('Product ID has been changed successfully.')

    def display_product_details(self):
        print(f"""
              PRODUCT DETAILS
              ---------------
              Supermarket name: {self.supermarket_name}
              Product ID: {self.__product_ID}
              Name: {self.name}
              Price: {self.price}
              Manufacturer: {self.manufacturer}
              Weight: {self.weight}
              Expiration date: {self.expiration_date}
              Year: {self.year}
      -------------------------------------------------
        """)
    def Product_subSystem_interface(self):
        print("""
        -- Welcome to Product Sub-system --
        to navigate through, enter your command:
        1. to Add new product.
        2. to Display product details.
        3. to Change/edit product ID.
        4. to Exit this sub-system.
        5. to Exit the supermarket cashier system.
        """)
        while True:
            try:
                option = int(input('Enter your command: '))
            except ValueError:
                print('Error, pls enter one number: ')
                continue
            if option == 1:
                self.add_new_product()
            elif option == 2:
                self.display_product_details()
            elif option == 3:
                self.change_productID()
            elif option == 4:
                self.main_menu()
            elif option == 5:
                exit()
    def main_menu(self):
        print("""
                           WELCOME TO OUR SUPERMARKET:
                           --------------------------
              PLEASE CHOOSE YOUR CATEGORY:
              1. PRODUCT SUB-SYSTEM > ENTER '1'
              2. HEALTHY PRODUCT SUB-SYSTEM > ENTER '2'
              3. TO EXIT THE SUPERMARKET CASHIER > ENTER '3'
                 -----------------------------------------------
              """)
        while True:
            try:
                option = int(input('enter 1, 2 or 3 '))
            except ValueError:
                print('Error, please choose only one 1, 2, 3')
                continue
            else:
                if option == 1:
                    self.Product_subSystem_interface()
                elif option == 2:
                    healthy_instance.Healthyproduct_userInterface()
                else:
                    print(' THANKS FOR USING OUR SUPERMARKET SYSTEM :) ')
                    exit()
class Healthy(Product):
    def __init__(self,supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year, calories=0, components=""):
        super().__init__(supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year)
        self.calories = calories
        self.components = components

    def add_new_Healthy_product(self):
        self.name = input('Enter the name of the new product: ')
        self.price = float(input('Enter the price of the new product: '))
        self.manufacturer = input('Enter the manufacturer of the new product: ')
        self.weight = float(input('Enter the weight of the new product: '))
        self.expiration_date = input('Enter the expiration date of the new product: ')
        self.year = input('Enter the year of the new product: ')
        self.__product_ID = random.randint(10000, 1000000)
        self.calories = int(input('Enter calories: '))
        self.components = input('Enter components: ')
        print('Healthy product added successfully.')

    def change_calories(self):
        self.calories = int(input('Change calories: '))

    def display_Healthy_product_details(self):
        print(f"""
          HEALTHY PRODUCT DETAILS
              ---------------
              Supermarket name: {self.supermarket_name}
              Product ID: {self._Product__product_ID}
              Name: {self.name}
              Price: {self.price}
              Manufacturer: {self.manufacturer}
              Weight: {self.weight}
              Calories: {self.calories}
              Components: {self.components}
              Total Calories: {self.total_calories_based_on_the_weight_entered()}
              Expiration date: {self.expiration_date}
              Year: {self.year}
          ----------------------------------------
        """)

    def check_caloriesAndcomponents_ofHealthyProduct(self):
        print(f'Your Healthy product calories:{self.calories} (G), its components: {self.components}')

    def total_calories_based_on_the_weight_entered(self):
        total = self.weight * self.calories
        print(f'Total calories of this healthy product based on the weight you entered is: {total}')

    def Healthyproduct_userInterface(self):
        print("""
        -- Welcome to Healthy Product Sub-system --
        to navigate through, enter your command:
        1. to Add new healthy product.
        2. to Display healthy product details.
        3. to Change/edit calories.
        4. to Check calories and components of healthy product.
        5. to Compute total calories of the healthy product based on provided weight.
        6. to Exit this sub-system.       
        7. to Exit the supermarket cashier system.
        """)
        while True:
            try:
                option = int(input('Enter 1, 2, 3, 4, 5, 6 or 7: '))
            except ValueError:
                print('Error, pls enter one number: ')
                continue
            if option == 1:
                self.add_new_Healthy_product()
            elif option == 2:
                self.display_Healthy_product_details()
            elif option == 3:
                self.change_calories()
            elif option == 4:
                self.check_caloriesAndcomponents_ofHealthyProduct()
            elif option == 5:
                self.total_calories_based_on_the_weight_entered()
            elif option == 6:
                self.main_menu()
            elif option == 7:
                exit()


    def main_menu(self):
        print("""
                           WELCOME TO OUR SUPERMARKET:
                           --------------------------
              PLEASE CHOOSE YOUR CATEGORY:
              1. PRODUCT SUB-SYSTEM > ENTER '1'
              2. HEALTHY PRODUCT SUB-SYSTEM > ENTER '2'
              3. TO EXIT THE SUPERMARKET CASHIER > ENTER '3'
                 -----------------------------------------------
              """)
        while True:
            try:
                option = int(input('enter 1, 2 or 3 '))
            except ValueError:
                print('Error, please choose only one 1, 2, 3')
                continue
            else:
                if option == 1:
                    self.Product_subSystem_interface()
                elif option == 2:
                    self.Healthyproduct_userInterface()
                else:
                    print(' THANKS FOR USING OUR SUPERMARKET SYSTEM :) ')
                    exit()

supermarket_name = "Your Supermarket Name"
product_instance = Product(supermarket_name=supermarket_name, product_ID=123, name="Sample Product", price=10.99, manufacturer="Sample Manufacturer", weight=100, expiration_date="2024-12-31", year="2024")
healthy_instance = Healthy(supermarket_name=supermarket_name, product_ID=123, name="Sample Product", price=10.99, manufacturer="Sample Manufacturer", weight=100, expiration_date="2024-12-31", year="2024")

product_instance.main_menu()
healthy_instance.main_menu()