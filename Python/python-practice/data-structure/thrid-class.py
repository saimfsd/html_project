def login():
    # predefined username, email, and password
    username = "divya123"
    email = "divya@example.com"
    password = "mypassword"

    # user input
    userUsername = input("Enter username or email: ")
    userPassword = input("Enter password: ")

    # login condition (same logic as in your C code)
    if (userUsername == username or userUsername == email) and userPassword == password:
        print("Login successful")
    else:
        print("Login failed")


def main():
    login()


 
if __name__ == "__main__":
    main()
