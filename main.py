class Customer():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Customer :{self.name}>"
    
class Coffee():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Coffee: {self.name}>"
    
class Order():
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        self.price =  price 
    def __repr__(self):
        return f"Order for {self.customer.name} :{self.coffee.name}"

if __name__ == "__main__":
    print("***********Welcome to Zen House Coffee Shop**********")

    
    # New Customer objects (Trend-based for 2026)
    customer1 = Customer("Atlas")
    customer2 = Customer("Seraphina")
    customer3 = Customer("Jasper")

    # New Coffee objects (Creative menu items)
    coffee1 = Coffee("Midnight Pour")
    coffee2 = Coffee("Lunar Latte")
    coffee3 = Coffee("Velvet Almond")

    # Processing orders with customer, coffee, and price
    order1  =  Order(customer1, coffee2, 4.50)  
    order2  =  Order(customer2, coffee1, 5.25)  
    order3  =  Order(customer3, coffee3, 6.00)  
    order4  =  Order(customer1, coffee2, 5.75)  
    order4  =  Order(customer1, coffee2, 5.75)  

    print(order1)
    print(order2)
    print(order1)
    print(order4)