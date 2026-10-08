while True:
    password = input("Enter password (or 'stop' to exit): ")

    if password == "stop":
        print("Program stopped.")
        break

    if len(password) >= 8 and \
       any(c.isupper() for c in password) and \
       any(c.islower() for c in password) and \
       any(c.isdigit() for c in password):

        print("Strong password")
    else:
        print("Weak password")