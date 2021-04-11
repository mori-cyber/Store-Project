

def read_from_database():
    try:
        products = []
        file = open("C:/Users/diana/Videos/project/database.csv", "r")
        file_read = file.read()
        product = file_read.split("\n")
        for i in range(len(product)):
            split = product[i].split(",")
            products.append({"id": split[0], "name": split[1], "price": split[2], "count": split[3]})

    except Exception as e:
        print(e)
        products = []

    return products

5
products = read_from_database()


def show_menu():
    menu = ["1-Add New Product", "2-Search", "3-Edit", "4-Remove", "5-Buy", "6-Show_all", "7-Exit"]
    for item in menu:
        print(item)


def add():
    id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    price = int(input("Enter Price: "))
    count = int(input("Enter count: "))
    products.append({"id": id, "name": name, "price": price, "count": count})


def search():
    user_input = input('enter a text to search:')
    for product in products:
        if product['id']==user_input or product['name']==user_input:
            print('product')
    else:
        print('not found')
 
def edit():
   
    editor = input("Enter Choice: ")

    for product in products:
        if product["id"] == user_edit or product["name"] == user_edit:
            print("this is correct")
        u_product = input("Which Part To Edit? ")
        if u_product == "id":
            id = int(input("Enter New Id: "))
            product["id"] = id
            break
        elif u_product == "name":
            name = input("Enter New Name: ")
            product["name"] = name
            break
        elif u_product == "price":
            price = input("Enter New Price: ")
            product["price"] = price
            break
        elif u_product == "count":
            count = input("Enter New Count: ")
            product["count"] = count
            break
    else:
        print("not found  this item")


def remove():
    remove_item = input("Enter item: ")
    for product in products:
        if product["id"] == user_remove or product["name"] == user_remove:
            print("please remove this item:")
            products.remove(product)
            print("removed")
            break
    else:
        print("not found")


def buy():
    print("what product is need:" )
    p_remove = input("Enter product: ")
    for product in products:
        if product["id"] == p_remove or product["name"] == p_remove:
            print("this product is empty")
            p_count = input("Enter Number: ")
            if product["count"] > p_count:
                result = int(product["count"]) - int(p_count)
                print("rsolve it")
                break
            else:
                print("count is Not enough ")
                break
    else:
        print("count not found")


def show_all():
    for product in products:
        print('thank you for see my products:',product)


def all_exit():
    exit_from_database = input('enter yes for exit:')
    if exit_from_database == "yes":
        file = open("database.csv", "a")
        for product in products:
            file.write(str(f"\n{product}"))
            exit()
    else:
        exit()


while True:
    show_menu()
    user = int(input("\nEnter Number: "))
    if user == 1:
        add()
    elif user == 2:
        search()
    elif user == 3:
        edit()
    elif user == 4:
        remove()
    elif user == 5:
        buy()
    elif user == 6:
        show_all()
    elif user == 7:
        all_exit()