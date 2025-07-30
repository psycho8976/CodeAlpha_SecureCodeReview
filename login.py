import hashlib

# Load users and their hashed passwords from file
def load_users():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, hashed_password = line.strip().split(",")
                users[username] = hashed_password
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    return users

# Hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login logic with 3 attempt limit
def login(users):
    attempts = 3
    while attempts > 0:
        uname = input("Enter username: ").strip()
        pwd = input("Enter password: ").strip()
        hashed_pwd = hash_password(pwd)

        if uname in users and users[uname] == hashed_pwd:
            print("✅ Login successful!")
            return
        else:
            attempts -= 1
            print(f"❌ Access denied. Attempts left: {attempts}")

    print("🔒 Too many failed attempts. Try again later.")

# Main execution
if __name__ == "__main__":
    users = load_users()
    if users:
        login(users)
