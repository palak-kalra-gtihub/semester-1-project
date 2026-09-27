user_pass_dict={'palakkalra':'abc123', 'mannatkaur':'rockyou', 'ginagina':'thebest', 'xielian':'3timesgod', 'huacheng':'ghostking'}
inventory=[['Name', 'Artist', 'Price', 'Release Year', 'Quantity'], ['Thriller', 'Micheal Jackson', 1500, 1982, 10], ['Back in Black', 'AC/DC', 1000, 1980, 6], ['The Dark Side of the Moon', 'Pink Floyd', 1240, 1973, 4], ['Abbey Road', 'The Beatles', 1600, 1969, 6], ['Nevermind', 'Nirvana', 1200, 1991, 2], ['Purple Rain', 'Prince', 2000, 1984, 4], ['Hotel California', 'Eagles', 1800, 1976, 1], ['Rumours', 'Fleetwood Mac', 1850, 1977, 9], ['Bat Out Of Hell', 'Meat Loaf', 1900, 1977, 3], ['Come on over', 'Shania Twain', 2100, 1997, 5], ['Saturday Night Fever', 'The Bee Gees', 1900, 1977, 5]]
emp_pass_dict={'0001':'iamgod','0002':'myfirstjob', '0003':'asdfgjkl;', '0004':'wowpass'}
emp_info_dict={'0001':['Dhruv Sharma', 24, '1234 Maple Drive', 10000], '0002':['Aisha Sharma', 22, '1234 Maple Drive', 8000], '0003':['George King', 30, 'Christ Heights', 15000], '0004':['Shaun Sheep', 15, 'Empire Society', 5000]}
total_money=123000
subtotal=0
cart=[]

def add_to_cart():
    rec_name=input("Enter which record you would like to add to cart").lower()
    for i in range(1, len(inventory)):
        if inventory[i][0].lower() == rec_name:
            if inventory[i][4] > 0:
                found = False
                for j in range(1, len(cart)):
                    if cart[j][0] == rec_name:
                        cart[j][4] += 1
                        found = True
                if found == False:
                    record = [inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3], 1]
                    cart.append(record)
                inventory[i][4] -= 1
                print("Record added to cart.")
            else:
                print("Record is out of stock.")
                
def delete_cart():
    rec_name = input("Enter record you would like to delete : ").lower()
    rec_quantity = int(input("Enter quantity to delete : "))
    for i in range(1, len(cart)):
        if cart[i][0].lower() == rec_name:
            if rec_quantity <= cart[i][4]:
                cart[i][4] = cart[i][4] - rec_quantity
                for j in range(1, len(inventory)):
                    if inventory[j][0] == rec_name:
                        inventory[j][4] = inventory[j][4] + rec_quantity
                if cart[i][4] == 0:
                    cart.pop(i)
                print("Record removed from cart.")
            else:
                print("You don't have that many copies in your cart.")

            break

def search_name():
    rec_name=input("Enter name of record to search for : ").lower()
    print("Here's the inventory : ")
    for i in inventory:
        if i[0].lower()==rec_name:
            print(i)
            
def search_artist():
    rec_artist=input("Enter artist to search for : ").lower()
    print("Here's the inventory : ")
    for i in inventory:
        if i[1].lower()==rec_artist:
            print(i)
        
def search_year():
    rec_year=int(input("Enter year you would like to search for : "))
    print("Here's the inventory : ")
    for i in inventory:
        if i[3]==rec_year:
            print(i)
            
def search_price():
    lower=int(input("Enter lowest amount : "))
    higher=int(input("Enter highest amount : "))
    print("Here's the inventory : ")
    for i in inventory:
        if i[2]>=lower and i[2]<=higher :
            print(i)
            
def view_cart():
    global subtotal
    if cart==[]:
        print("Cart Empty. Time to fill it up!")
    else:
        print("Here's your cart : ")
        for i in cart:
            print(i)
            subtotal+=(i[2]*i[4])
        print("Subtotal : ", subtotal)

def check_out():
    global subtotal
    global cart
    global total_money
    print("Checked Out! Your order will arrive in 9 buisness days.")
    total_money+=subtotal
    cart=[]
    
    
    
def view_inventory():
    print("Here's the inventory : ")
    for i in inventory:
        print(i)

def add_employee():
    emp_id=input("Enter new employee ID : ")
    if emp_id in emp_info_dict:
       print("Employee ID already exists")
    else:
        emp_pass=input("Enter new employee password : ")
        emp_name=input("Enter employee name : ")
        emp_age=int(input("Enter employee age : "))
        emp_address=input("Enter employee's address : ")
        emp_salary=int(input("Enter employee's salary : "))
        emp_pass_dict[emp_id]=emp_pass
        emp_info_dict[emp_id]=[emp_name,emp_age,emp_address,emp_salary]
    
def delete_employee():
    emp_id=input("Enter employee ID : ")
    if emp_id in emp_info_dict and emp_id in emp_pass_dict : 
        del emp_info_dict[emp_id]
        del emp_pass_dict[emp_id]
        print("Employee deleted")
    else:
        print("Employee not found")
    

def edit_employee_info():
    emp_id=input("Enter employee id : ")
    if emp_id in emp_info_dict and emp_id in emp_pass_dict:
        print("What information would you like to edit?")
        print("1. Password")
        print("2. Name")
        print("3. Age")
        print("4. Address")
        print("5. Salary")
        i=int(input("(1/2/3/4/5) : "))
        if i == 1:
            passwd=input("Enter new password : ")
            emp_pass_dict[emp_id]=passwd
        elif i==2:
            emp_name=input("Enter new name : ")
            emp_info_dict[emp_id][0]=emp_name
        elif i==3:
            emp_age=int(input("Enter new age : "))
            emp_info_dict[emp_id][1]=emp_age
        elif i==4:
            emp_address=input("Enter new address : ")
            emp_info_dict[emp_id][2]=emp_address
        elif i==5:
            emp_salary=int(input("Enter new salary : "))
            emp_info_dict[emp_id][3]=emp_salary
        else :
            print("Invalid choice")
    else:
        print("Employee not found")

def view_employee_info():
    for i in emp_info_dict:
        print(i, emp_info_dict[i])

def add_inventory():
    rec_name=input("Enter record name : ")
    rec_artist=input("Enter artist name : ")
    rec_price=int(input("Enter price : "))
    rec_year=int(input("Enter release year : "))
    rec_quantity=int(input("Enter Quantity : "))
    record=[rec_name,rec_artist,rec_price,rec_year,rec_quantity]
    if record not in inventory: 
        inventory.append(record)
    else:
        print("Record already in inventory")
    
def delete_inventory():
    rec_name = input("Enter record name to delete : ")
    if rec_name in inventory:
        for i in range(1, len(inventory)):
            if inventory[i][0] == rec_name:
                inventory.pop(i)
                print("Record deleted")
    else:
        print("Record not found")
        
def edit_inventory():
    rec_name=input("Enter record name : ")
    print("What do you want to edit?")
    print("1. Name")
    print("2. Artist Name")
    print("3. Price")
    print("4. Release Year")
    print("5. Quantity")
    i=int(input("(1/2/3/4/5) : "))
    if i == 1:
        recname=input("Enter new record name : ")
        for j in inventory:
            if j[0]==rec_name:
                j[0]=recname
                print("Updated")

    elif i == 2:
        rec_artist=input("Enter new artist name : ")
        for j in inventory:
            if j[0]==rec_name:
                j[1]=rec_artist
                print("Updated")

    elif i == 3:
        rec_price=int(input("Enter new price : "))
        for j in inventory:
            if j[0]==rec_name:
                j[2]=rec_price
                print("Updated")

    elif i == 4:
        rec_year=int(input("Enter new year : "))
        for j in inventory:
            if j[0]==rec_name:
                j[3]=rec_year
                print("Updated")

    elif i == 5:
        rec_quantity=int(input("Enter new quantity"))
        for j in inventory: 
            if j[0]==rec_name:
                j[4]=rec_quantity
                print("Updated")
    else:
        print("Invalid Choice")
        
def check_money():
    print("The amount of money you current have is : ", total_money)

def edit_money():
    global total_money
    new_money=int(input("Enter updated money : "))
    total_money=new_money
    
def pay_salary():
    global total_money
    salary = 0
    for i in emp_info_dict:
        salary += emp_info_dict[i][3]
    if salary <= total_money:
        total_money -= salary
        print("Salaries paid successfully.")
    else:
        print("Not enough money to pay salaries.")
        

print("====================================================================")
print("Welcome to the records store")
print("====================================================================")
print("Who are you entering as?")
print("1. Owner")
print("2. Employee")
print("3. Customer")
ans=int(input("(1/2/3): "))
print()
if ans==1:
    access=False
    for i in range(3):
       password_check=input("Enter owner's password : ")
       if password_check=='IamTheOwnerLetMeIn':
           print("Acess Granted.")
           access=True
           break
       else:
            print("Incorrect password. You have", (2-i), "attempts left.")
    else :
       print("You are not the owner.") 
    
    if access==True:
        while True:
            print()
            print("====================================================================")
            print("What would you like to do?")
            print("1. View employee information")
            print("2. Add employee")
            print("3. Delete employee")
            print("4. Edit employee information")
            print("5. View inventory")
            print("6. Add to inventory")
            print("7. Delete from inventory")
            print("8. Edit inventory information")
            print("9. Check money")
            print("10. Edit money")
            print("11. Pay salaries")
            print("12. Exit")
            print()
            what_ans=int(input("(1/2/3/4/5/6/7/8/9/10/11/12): "))
            print("====================================================================")
            print()
            if what_ans==1:
                view_employee_info()
            elif what_ans==2:
                add_employee()
            elif what_ans==3:
                delete_employee()
            elif what_ans==4 :
                edit_employee_info()
            elif what_ans==5:
                view_inventory()
            elif what_ans==6:
                add_inventory()
            elif what_ans==7:
                delete_inventory()
            elif what_ans==8:
                edit_inventory()
            elif what_ans==9:
                check_money()
            elif what_ans==10:
                edit_money()
            elif what_ans==11:
                pay_salary()
            elif what_ans==12:
                break
            else :
                print("Invalid Choice")
            
elif ans==2:
    access=False
    emp_id=input("Enter your employee ID : ")
    if emp_id in emp_pass_dict:
        for i in range(3):
           password_check=input("Enter your password : ")
           if password_check==emp_pass_dict[emp_id]:
               print("Acess Granted.")
               access=True
               break
           else:
                print("Incorrect password. You have", (2-i), "attempts left.")
        else :
           print("You are not the employee.")
        if access==True:
            while True : 
                print()
                print("====================================================================")
                print("What would you like to do?")
                print("1. View inventory")
                print("2. Add to inventory")
                print("3. Delete from inventory")
                print("4. Edit inventory information")
                print("5. Exit")
                what_ans=int(input("(1/2/3/4/5) : "))
                print("====================================================================")
                print()
                if what_ans==1:
                    view_inventory()
                elif what_ans==2:
                    add_inventory()
                elif what_ans==3 : 
                    delete_inventory()
                elif what_ans==4 :
                    edit_inventory()
                elif what_ans==5:
                    break
                else:
                    print("Invalid Choice")
    else:
        print("You are not a registered employee")
        
if ans==3:
    access=False
    ans1=input("Do you have an account with us? (y/n)?")
    if ans1=='n':
        user=input("Enter new username : ")
        passwd=input("Enter password : ")
        user_pass_dict[user]=passwd
    elif ans1=='y':
        access=False
        user=input("Enter your username : ")
        if user in user_pass_dict:
            for i in range(3):
               password_check=input("Enter password : ")
               if password_check==user_pass_dict[user]:
                   print("Acess Granted.")
                   access=True
                   break
               else:
                    print("Incorrect password. You have", (2-i), "attempts left.")
            else: 
                print("You are not the account holder")
            if access==True:
                while True : 
                    print()
                    print("====================================================================")
                    print("What would you like to do?")
                    print("1. View inventory")
                    print("2. Search for record")
                    print("3. Search for artist")
                    print("4. Search for Year")
                    print("5. Search according to price")
                    print("6. View Cart")
                    print("7. Add to cart")
                    print("8. Delete from cart")
                    print("9. Check Out")
                    print("10. Exit")
                    ans2=int(input("(1/2/3/4/5/6/7/8/9/10) : "))
                    print("====================================================================")
                    print()
                    if ans2==1:
                        view_inventory() 
                    elif ans2==2:
                        search_name()
                    elif ans2==3:
                        search_artist()
                    elif ans2==4:
                        search_year()
                    elif ans2==5:
                        search_price()
                    elif ans2==6:
                        view_cart()
                    elif ans2==7:
                        add_to_cart()
                    elif ans2==8:
                        delete_cart()
                    elif ans2==9:
                        check_out()
                    elif ans2==10:
                        break
                    else:
                        print("Invalid choice.")
                            