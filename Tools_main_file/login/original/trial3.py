from trial32 import accounts
f = open("trial32.py")
def main():
    import time
    import random

    ins = True
    while ins == True:
        user = str(input("admin or user or creating account? (admin/user/c)    "))
        if user == "c":
            a_u = input("creating admin account or user account? (a/u)     ")
            if a_u == "a":
                pas = input("Please input your admin account creating pass:     ")
                if pas == "1234":
                    print("ok, leading you to creat admin account...")
                    creat_a()
                    return
                else:
                    print("sorry, you have the wrong pass, leading you to the beginning...")
            if a_u == "u":
                print("ok, leading you to creating user account.")
                creat_u()
                return
        elif user == "admin":
            login_a()
            return
        elif user == "user":
            login_u()
            return

    return


def login_u():
    user_input = str(input("username     "))
    if user_input in accounts ["user"]:
        name = True
        while name == True:
            user_input2 = input("Password:     ")
            if user_input2 in accounts["user"][user_input]:
                print("You succesfully loged in.")
                ins = False
                log = False
                users()
                return

            elif not user_input2 in accounts["user"][user_input]:
                print("Password is incorrect.")
    if not user_input in accounts["user"]:
        print(f"We do not have this username in user.")
        main()

    return


def login_a():
    user_input = str(input("username     "))
    if user_input in accounts ["admin"]:
        name = True
        while name == True:
            user_input2 = input("Password:     ")
            if user_input2 in accounts["admin"][user_input]:
                print("You succesfully loged in.")
                ins = False
                log = False
                admins()
                return

            elif not user_input2 in accounts["admin"][user_input]:
                print("Password is incorrect.")
    if not user_input in accounts["admin"]:
        print(f"We do not have this username in admin.")
        main()

    return


def admins():
    ue = input()
    print(ue)
    print("Thank you for logging in, admin.")
    return


def users():
    user = input("123")
    print(user)
    print("Thank you for logging in, user.")
    return

def creat_u():
    creating = True
    while creating == True:
        new_u = input("Type your username:     ")
        if new_u in accounts["user"]:
            print("This username already exist.")
        else:
            new_p = input("Type your password:       ")
            accounts["user"][new_u] = new_p
            
            #print(accounts["user"])
            print(f"username: {new_u}, password: {new_p}")
            s = input("is this your username and password? (y/n)     ")
            if s == "y":
                print("ok, leading you to login")
                creating = False
                login_u()
                
                
    return

def creat_a():
    creating = True
    while creating == True:
        new_a = input("Type your username:     ")
        if new_a in accounts["admin"]:
            print("This username already exist.")
        else:
            new_p = input("Type your password:     ")
            #accounts["admin"][new_a] = new_p
            #print(accounts["admin"])
            print(f"username: {new_a}, password: {new_p}")
            s = input("is this your username and password? (y/n)     ")
            if s == "y":
                accounts["admin"][new_a] = new_p
                print("ok, leading you to login")
                creating = False
                login_a()
                return
            if s == "n":
                print("ok, leading you to recreat.....")
                accounts["admin"].pop(new_a)
            
    return





























if __name__ == "__main__":
    main()
