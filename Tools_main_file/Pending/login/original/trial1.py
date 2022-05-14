accounts = {

        "admin" : {
            "A" : "1234",
            },


        "user" : {
            "1" : "2345",
            }
        }


def main():
    import time
    import random
##    accounts = {
##
##        "admin" : {
##            "A" : "1234",
##            },
##
##
##        "user" : {
##            "1" : "2345",
##            }
##        }
    ins = True
    while ins == True:
        user = str(input("admin or user or creating account? (admin/user/c)    "))
        if user == "c":
            creat()
        else:
            user_input = str(input("username     "))
            if user_input in accounts [user]:
                log = True
                while log == True:
                    user_input2 = input("Password:     ")
                    if user_input2 in accounts[user][user_input]:
                        print("You succesfully loged in.")
                        ins = False
                        log = False

                        if user == "admin":
                            admin()
                            

                        elif user == "user":
                            users()
                            ins = False

                        else:
                            print("Thank you")
                            ins = False
                        
                    elif not user_input2 in accounts[user][user_input]:
                        print("Password is incorrect.")
            if not user_input in accounts[user]:
                print(f"We do not have this username in {user}")
                main()

    return accounts


def admin():
    ue = input()
    print(ue)
    return

def users():
    user = input("123")
    print(user)

def creat():
    creating = True
    while creating == True:
        new_u = input("Type your username:     ")
        if new_u in accounts["user"]:
            print("This username already exist.")
        else:
            new_p = input("Type your password:       ")
            accounts["user"][new_u] = new_p
            #print(accounts["user"])
            print(accounts["user"][new_u])
            s = input("is this your username and password? (y/n)     ")
            if s = "y":
                print("ok, leading you to login")
                
    return































if __name__ == "__main__":
    main()
