# Zen House Coffee Shop ☕
A Python-based command-line application that models a coffee shop domain using Object-Oriented Programming (OOP). This project demonstrates many-to-many relationships between Customers, Coffee types, and Orders.
## 🚀 Features
Robust Validation: Ensures names and prices meet specific length and range requirements.
Object Relationships: Tracks unique associations between customers and their coffee preferences.
Aggregate Analytics: Calculates total orders and average prices per coffee.
Bonus - Most Aficionado: A class method that identifies the customer who has spent the most on a specific coffee.
## 🛠️ Project Setup
Follow these steps to set up the repository and run the application in your local environment.
1. Create a Project Folder
bash
mkdir coffee-shop
cd coffee-shop


2. Set Up a Virtual Environment
It is best practice to use a virtual environment to manage dependencies.
bash
## Create the environment
```   python -m venv venv```

## Activate on Windows
venv\Scripts\activate

## Activate on macOS/Linux
source venv/bin/activate

3. Running the Application
Once the environment is active, you can run the main script to see the sample output:
bash
python main.py
Use code with caution.

## 📂 Domain Model
The project is structured around three core classes:
**Customer**: Manages customer names and their order history.
**Coffee**: Manages the menu items and provides aggregate data (number of orders, average price).
**Order**: The "Single Source of Truth" that connects a specific customer to a specific coffee with a unique price.
### 📝 Usage Example
``` python
# Create instances
atlas = Customer("Atlas")
latte = Coffee("Lunar Latte")

# Create an order
order = atlas.create_order(latte, 5.50)

# View statistics
print(f"Total orders for {latte.name}: {latte.num_orders()}")
print(f"Top spender: {Customer.most_aficionado(latte)}")


### 📜 Requirements Check
* Names are strings (Customer: 1-15 chars, Coffee: 3+ chars).
* Coffee names are immutable after instantiation.
Order prices are floats between 1.0 and 10.0 and are immutable.
* Returns unique lists for many-to-many relationships.
