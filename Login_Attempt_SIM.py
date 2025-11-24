#Stephen Hernandez
#extra credit

import time
def Login_sim():
    password = "bob123!"

    print("please enter password" )
    failed_attempt = 0

    while True:
        correct_password = "bob123!"


        user_entered_password = input()


        if correct_password == user_entered_password:
            print("Access Granted")

            break



        else:
            if user_entered_password != correct_password:
                print("Wrong Password")
            failed_attempt += 1
            if failed_attempt == 3:
                print("Access Denied")
                break






if __name__ == "__main__":
    Login_sim()