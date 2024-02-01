from cryptography.fernet import Fernet
import bcrypt

def generate_access_key():  # generate the software license/product key
    key = Fernet.generate_key() # a strong random key is generated
    key_str = str(key).removeprefix("b'").removesuffix("='")
    return key_str

def hash_key(key):
    hashed_key= bcrypt.hashpw(key.encode('utf-8'), bcrypt.gensalt()) # hash the access key using bcrypt
    return hashed_key

if __name__ == "__main__":
    access_key = generate_access_key()
    hash_of_key = hash_key(access_key) # you can store this hash in the database
    print(f"Generated key : {access_key}")
    # print(hash_of_key)
