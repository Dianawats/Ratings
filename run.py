if __name__ =="__main__":
    welcome_page ='\n Welcome to the Bootcamper\n1. Bootcamper\n.2 LFA \n.3 LF'
    run_app = True
    while run_app:
       print (welcome_page)
       selection = int(input("selection: "))
       if 0 <= selection >= 4:
            print("Option does not exist, please try again")
            continue
       else:  # In case of a valid input, run code for either option selected
            # Allows a user to sign up
            if selection is 1:
               print("\nCreate a new account")
                # get the name of the user
               name = input("Enter your name: ")
                # Allows a user to enter his/her password
               password = input("Enter your password: ")
            if selection is 2:
               print("\nCreate a new account")
                # get the name of the LFA
               name = input("Enter your name: ")
                # Allows a LFA to enter his/her password
               password = input("Enter your password: ")

            if selection is 3:
                pass
