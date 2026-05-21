import time

class Pepperoni:
    @classmethod
    def prepare_pizza(cls):
        print ("One pepperoni pizza coming right up!","\n")
        time.sleep(1)
        print ("Adding pepperonis...","\n")
        time.sleep(1)
        print ("Adding cheese and sauce...")
    @classmethod
    def ready(cls):
        print("One pepperoni pizza is done")
class Veggie:
    @classmethod
    def prepare_pizza(cls):
        print ("One veggie pizza coming right up!","\n")
        time.sleep(1)
        print("Adding vegetables...","\n")
        time.sleep(1)
        print("Adding cheese and the sauce")
    @classmethod
    def ready(cls):
        print ("Veggie pizza is done")
class Extra_Cheese:
    @classmethod
    def prepare_pizza(cls):
        print ("One Extra Cheese pizza coming right up!","\n")
        time.sleep(1)
        print("Adding cheese...","\n")
        time.sleep(1)
        print("Adding extra cheese and the sauce")
    @classmethod
    def ready(cls):
        print ("Extra cheese pizza is done")
    