# Hi, Welcome to my mini project of playing around with Python. Try it yourself! It is just a login program with a little surprise :) 

# Sign Up Form

def signup():
    while True:
        username = input("Enter your new username:")
        password = input("Enter your new password:")

        if len(username) > 3 and len(password) > 8:
            print("Welcome to the system!")
            return username, password
        else:
            print("Username should have a minimum of 3 characters & Password should have a minimum of 8 characters")

username, password = signup()

# Secret admin login
logininfo = (username, password)

def hack(code):
    if code == "1892":
        print(logininfo)
    else:
        print("Not a chance!")

#Sign In Form

def signin():
    while True:
        users_name = input("To log into your account, please enter your username:")
        users_password = input("And your password:")
        if users_name == username and users_password == password:
            print("You are in!")
            return users_name, users_password
        else:
            print("Wrong username or password\n")
            hack(input("Or enter a special code to see your info:"))
            
users_name, users_password = signin()

print("Thank you so much for trying out my program :)")
