import string

common_passwords = [
    "password123", "1234567890", "qwertyuiop", "letmein123", "welcome@123",
    "iloveyou123", "admin1234", "abc12345678", "pass@word1", "password@123",
    "supersecure", "mypassword", "default@123", "sunshine123", "login@123"
]

while True:
    status = []
    print("\n==============================")
    print("🔐  PASSWORD STRENGTH CHECKER")
    print("==============================")
    username = input("\nEnter Your username : ")
    password = input("Enter Your Password to check : ")

    # checking same as username
    if password != username:
        status.append("your password not same as the username ✅")
    else:
        status.append("Your password is same as the username ❌")

    if len(password) >= 12:
        status.append("your password length is good ✅")
    else:
        status.append("your password is too short ❌ (min 12 characters)")


    #checking lower case
    if any(char.isupper() for char in password):
        status.append("Your password contain capital ✅")
    else:
        status.append("your password not contains capital ❌")

    #checking uppercase
    if any(char.islower() for char in password):
        status.append("your password contian lowercase ✅")
    else:
        status.append("your password not contains lower case ❌")

    #cheking digit
    if any(char.isdigit() for char in password):
        status.append("your password contain digit ✅")
    else:
        status.append("your password not contain digit ❌")
    
    #checking special char
    if any(char in string.punctuation for char in password):
        status.append("your password contain special character ✅")
    else:
        status.append("your password not contain special character ❌")

    #checking common passwords
    if password not in common_passwords:
        status.append("your password not a common ✅")
    else:
        status.append("your Password is too common ❌")
    
    # Show status
    print("\n🔎 Password Check Report:")
    for s in status:
        print("-", s)

    # Final Result
    if all("✅" in s for s in status):
        print("\n✅ Password is STRONG and secure!")
    else:
        print("\n❌ Password is WEAK. Please try again.")

    # Ask to retry
    retry = input("\nDo you want to check another password? (y/n): ").lower()
    if retry != 'y':
        break
