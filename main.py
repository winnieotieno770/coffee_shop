class Customer():
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value,str) and 1<= len(value) <= 15:
            self._name = value
        else :
            raise TypeError("Must be a string betwen 1 to 15 characters")
        
    def create_order(self,coffee,price):
        return Order(self,coffee,price)

    def orders(self):
        return [order for order in Order.all if order.customer == self] 
    def coffees(self):
        return [order.coffee for order in Order.all if order.customer == self]
    
    def __repr__(self):
        return f"<Customer :{self.name}>"
   
    @classmethod
    def most_aficionado(cls, coffee):
        if not cls.all:
            return None
        
        # Track the top spender and their maximum amount
        top_spender = None
        max_spent = 0

        for customer in cls.all:
            # Calculate total spent by this customer on the specific coffee instance
            total_for_customer = sum([
                order.price for order in Order.all 
                if order.customer == customer and order.coffee == coffee
            ])
            
            # Update top spender if this customer spent more
            if total_for_customer > max_spent:
                max_spent = total_for_customer
                top_spender = customer

        return top_spender

    
class Coffee():
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after it is set")
        
      
        if isinstance(value,str) and  len(value) >= 3:
            self._name = value
        else :
            raise TypeError("Must be a string  of characters 3 or more")
        
    def orders(self):
        return[order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return [order.customer for order in Order.all if order.coffee == self]
    
    def coffee_num_orders(self):
        orders = len(self.orders())
        if orders == 0:
            return 0
        else:
           return orders
    def average_price(self):
        if not self.orders():
            return 0
        else:
             prices = [order.price for order in self.orders()]
             return sum(prices) / len(self.orders())
    def __repr__(self):
        return f"<Coffee: {self.name}>"
    
class Order():
    all = []
    def __init__(self,customer,coffee,price):
        if isinstance(customer, Customer):
            self.customer = customer
        if isinstance(coffee, Coffee):    
           self.coffee = coffee

        self.price =  price 
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if hasattr(self, "_price"):
            raise AttributeError("Order price cannot be changed after it is set")
        if isinstance(value, float) and 1.0 <= value <= 10.0:
           self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
    
    def __repr__(self):
        return f"Customer {self.customer.name} Coffee Type:{self.coffee.name}"

if __name__ == "__main__":
    print("***********Welcome to Zen House Coffee Shop**********")

    
    # New Customer objects (Trend-based for 2026)
    customer1 = Customer("Atlas")
    customer2 = Customer("Seraphina")
    customer3 = Customer("Jasper")
    customer4 = Customer("Jaiden")
    customer5 = Customer("Allan")

    # New Coffee objects (Creative menu items)
    coffee1 = Coffee("Midnight Pour")
    coffee2 = Coffee("Lunar Latte")
    coffee3 = Coffee("Velvet Almond")
    coffee4 = Coffee("Capuchino")

    # Processing orders with customer, coffee, and price
    order1  =  Order(customer2, coffee2, 7.50)  
    order2  =  Order(customer2, coffee1, 5.25)  
    order3  =  Order(customer3, coffee1, 6.00)  
    order4  =  Order(customer1, coffee2, 5.75)  
    order5  =  Order(customer4, coffee2, 5.75)  
    
    customer5.create_order(coffee1,4.0)

    fan = Customer.most_aficionado(coffee2)
    if fan:
        print(f"Most Aficionado for {coffee1.name}: {fan.name}")
    else:
        print(f"No orders found for {coffee1.name}")

# print(customer2.orders())
print(customer5.name)
# print(coffee1.customers())
print(coffee4.coffee_num_orders())