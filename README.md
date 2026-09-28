# Project Objective

It is a simple Python-based project for managing a music records store. The main objective of this project isto demonstrate the use of the following Python programming concepts :
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Searching
* Updating data
* Adding and deleting data
* User authentication
* Basic inventory management
* Shopping cart management
* Financial calculations


# People You Can Enter as : 

## 1. Owner

The owner has access to the main management functions of the store. The owner can:
* View employee information
* Add new employees
* Delete employees
* Edit employee information
* View inventory
* Add records to inventory
* Delete records from inventory
* Edit inventory information
* Check the store's available money
* Edit the store's money
* Pay employee salaries


## 2. Employee

Employees can log in using their employee ID and password. Employees can:
* View inventory
* Add records to inventory
* Delete records from inventory
* Edit inventory information

## 3. Customer

Customers can either create a nt or log in using an existing account. Customers can:
* View the inventory
* Search for a record by name
* Search for records by artist
* Search for records by release year
* Search for records within a price range
* View their cart
* Add records to their cart
* Delete records from their cart
* Check out their order


# Inventory

The inventory contains the following information for each record:

| Field        | Description                  |
| ------------ | ---------------------------- |
| Name         | Name of the record           |
| Artist       | Artist or band               |
| Price        | Price of the record          |
| Release Year | Year the record was released |
| Quantity     | Number of copies available   |

# Cart System

The shopping cart contains the records the customer selected to purchase.
When a customer adds a record:
1. The program checks if the record is present.
2. The program checks if the record is in stock.
3. The quantity of the selected record is increased by one if the record is already in the cart.
4. If it is not present in the cart, add the record to it.
5. Reduce the quantity of the record in stock by one.

When a customer deletes:
1. Request the name of the record to delete.
2. Ask the customer to provide the quantity of the record.
3. Remove the record from the cart. If the quantity matches the cart’s quantity, delete the record completely from the cart.
4. Add the deleted record quantity to the record’s quantity in stock.

# Employee Management
Each employee has an Employee ID, Password, Name, Age, Address, and Salary

# Financial Management
The program keeps track of the store's available money using the `total_money` variable. The owner can check the current amount of money, update the amount, and pay employee salaries. The customer can check out their cart and pay for the whole cart. 

# Main Functions

| Function               | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| `add_to_cart()`        | Adds a record to the customer's cart      |
| `delete_cart()`        | Removes records from the cart             |
| `search_name()`        | Searches for a record by name             |
| `search_artist()`      | Searches for records by artist            |
| `search_year()`        | Searches for records by release year      |
| `search_price()`       | Searches for records within a price range |
| `view_cart()`          | Displays the customer's cart and subtotal |
| `check_out()`          | Completes the customer's order            |
| `view_inventory()`     | Displays all inventory                    |
| `add_employee()`       | Adds a new employee                       |
| `delete_employee()`    | Deletes an employee                       |
| `edit_employee_info()` | Changes employee information              |
| `view_employee_info()` | Displays employee information             |
| `add_inventory()`      | Adds a new record to inventory            |
| `delete_inventory()`   | Deletes a record from inventory           |
| `edit_inventory()`     | Changes record information                |
| `check_money()`        | Displays the store's available money      |
| `edit_money()`         | Changes the store's available money       |
| `pay_salary()`         | Pays all employee salaries                |

---

# Data Structures Used

## 1. Dictionaries

* `user_pass_dict` – customer usernames and passwords
* `emp_pass_dict` – employee IDs and passwords
* `emp_info_dict` – employee details

## 2. Lists

* `inventory` - all records information
* `cart` - records to be purchased by the customer

# Login System

The owner uses a separate password, while employees and customers use their respective IDs/usernames and passwords. Login attempts are limited to three attempts for everyone. 

# How to Run

1. Install **Python 3** on your computer.
2. Save the program as a `.py` file.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the program.
5. Run:

```bash
python untitled1.py
```
