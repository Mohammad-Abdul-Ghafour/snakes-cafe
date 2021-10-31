menu = {"Appetizers":["Wings","Cookies","Spring Rolls"],
    "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]}


def welcome_msg(menu):
    print(f"""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    ** To submit your order press Enter **
    **************************************
    """)

    for key in menu.keys():
        print(f"""
    {key}
    ----------""")
        for i in menu[key]:
            print(f"""    {i}""")
    
    print(f"""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """)
    quitFlag = ""
    while quitFlag != "quit" :
        order = input("    >" )
        if order == "quit":
            quitFlag = "quit"
            break
        elif order == "":
            print(f"""
    Your Orders are

            """)
            for key in ordered.keys():
                print(f"""    {key} : {ordered[key]}
    """)
            quitFlag = "quit"
            break
        else:
            orders(order)
    
ordered = {}
def orders(order):
    for key in menu.keys():
        time_breake = False
        for i in menu[key]:
            if str(order).lower() == str(i).lower():
                if str(order).lower() in ordered:
                    ordered[f"{str(order).lower()}"] += 1
                else:
                    ordered[f"{str(order).lower()}"] = 1

                print(f"""
    ** {ordered[f'{str(order).lower()}']} order of {i} have been added to your meal **
    """)
                time_breake = True
                break
        if time_breake == True :
            break
        elif key == list(menu)[-1]:
            print(f"""
    We are sorry we don't have {order}

            """)
        
               
                
if __name__=="__main__":
    welcome_msg(menu)