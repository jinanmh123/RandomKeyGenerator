import bcrypt

def hash_password(key):
    hashed_key = bcrypt.hashpw(key.encode('utf-8'), bcrypt.gensalt())
    return hashed_key

def verify_password(key, hashed_key):
    return bcrypt.checkpw(key.encode('utf-8'), hashed_key)


if __name__ == "__main__":
    stored_hashed_key = b'' # replace this with the hash stored in the database
    user_input_key = input("Enter Your Key : ")

    if verify_password(user_input_key, stored_hashed_key):
        print("Key is Valid. Authentication successful.")
    else:
        print("Key is invalid/expired.")
