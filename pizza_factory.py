from pizza_types import Pepperoni, Veggie, Extra_Cheese
import time
import re


class EmptyInputError(Exception):
    pass


class InvalidCharacterError(Exception):
    pass


class Pizza_Factory:
    @staticmethod
    def order_pizza():
        try:
            preference = input("Enter the pizza you wish for: ").strip().lower()

            if preference == "":
                raise EmptyInputError("Pizza choice cannot be empty")

            if not re.fullmatch(r"[a-zA-Z ]+", preference):
                raise InvalidCharacterError("Only letters and spaces are allowed")

            print("Checking if we have the pizza type you are asking for")
            time.sleep(3)
            print("\n")

            if preference == "pepperoni":
                Pepperoni.prepare_pizza()
                time.sleep(2)
                print("\n")
                Pepperoni.ready()

            elif preference == "veggie":
                Veggie.prepare_pizza()
                time.sleep(2)
                print("\n")
                Veggie.ready()

            elif preference == "extra cheese":
                Extra_Cheese.prepare_pizza()
                time.sleep(2)
                print("\n")
                Extra_Cheese.ready()

            else:
                print("We do not have this type of pizza")

        except EmptyInputError as e:
            print("Error:", e)

        except InvalidCharacterError as e:
            print("Error:", e)
            
        finally:
            print("Thanks for choosing our factory!")
            


try:
    Customer1 = Pizza_Factory()
    Customer1.order_pizza()
except KeyboardInterrupt:
    print("User stopped the program")