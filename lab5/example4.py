right_password = "abc123"
while True:
    password = input("Enter a password: ")
    if password == "help":
        print(right_password[0])
    elif password != right_password:
        print("Wrong!")
    else:
        print("Welcome")
        break