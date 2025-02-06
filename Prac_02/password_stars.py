def main():
    password = get_password()
    if check_min_length(password):
        print_password_stars(password)
    else:
        print("Password must be at least 8 characters long.")

def get_password():
    """User to enter a password"""
    return input("Enter your password: ")

def check_min_length(password):
    return len(password) >= 8

def print_password_stars(password):
    print('*' * len(password))

if __name__ == "__main__":
    main()