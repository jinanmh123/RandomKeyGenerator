from cryptography.fernet import Fernet
import secrets
import base64

def generate_access_key():
    # Generate a random key
    key = Fernet.generate_key()

    # Apply the fernet algorithm
    cipher_suite = Fernet(key)

    # Generate the random access key (combination of numbers and letters as you desired)
    access_key = base64.urlsafe_b64encode(cipher_suite.encrypt(secrets.token_bytes(32))).decode('utf-8')

    return access_key

if __name__ == "__main__":
    access_key = generate_access_key()
    print("Generated Key:", access_key)
