import hashlib
import random
import string

def generate_salt(length):
    characters = string.ascii_letters + string.digits
    salt = ''.join(random.choice(characters) for _ in range(length))
    return salt

def generate_hash(password, salt, hash_id):
    magic_strings = {
        "1": ("$1$", hashlib.md5),
        "2a": ("$2a$", hashlib.blake2b),
        "2y": ("$2y$", hashlib.blake2b),
        "5": ("$5$", hashlib.sha256),
        "6": ("$6$", hashlib.sha512)
    }

    if hash_id not in magic_strings:
        raise ValueError("Hash ID no válido")

    magic_string, hash_function = magic_strings[hash_id]
    combined_string = salt + password
    hash_object = hash_function(combined_string.encode())
    hashed_password = hash_object.hexdigest()
    return magic_string + salt + "$" + hashed_password

def main():
    password = input("Ingrese la contraseña: ")
    
    salt = generate_salt(8)
    print("Salt generado:", salt)

    print("Seleccione el algoritmo de hash:")
    print("1: MD5")
    print("2a: Blowfish")
    print("2y: Blowfish, with correct handling of 8 bit characters")
    print("5: SHA256")
    print("6: SHA512")

    hash_id = input("Ingrese el ID del algoritmo de hash: ")
    hashed_password = generate_hash(password, salt, hash_id)
    print("Contraseña hasheada:", hashed_password)

if __name__ == "__main__":
    main()
