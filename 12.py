from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()


def encrypt_message(message):
    message_bytes = message.encode('utf-8')
    rsa_public_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    encrypted_bytes = cipher_rsa.encrypt(message_bytes)
    return encrypted_bytes


def decrypt_message(encrypted_str):
    rsa_private_key = RSA.import_key(private_key)
    decipher_rsa = PKCS1_OAEP.new(rsa_private_key)
    decrypted_bytes = decipher_rsa.decrypt(encrypted_str)
    decrypted_message = decrypted_bytes.decode('utf-8')
    return decrypted_message


message = "oaoammm"

encrypted_message = encrypt_message(message)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
