import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Fixed key and IV
key = b'\x1a\x2b\x3c\x4d\x5e\x6f\x70\x81\x92\xa3\xb4\xc5\xd6\xe7\xf8\x09\x10\x21\x32\x43\x54\x65\x76\x87\x98\xa9\xba\xcb\xdc\xed\xfe\x0f'
iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

def encrypt(plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1212))
    server_socket.listen(1)
    print("Server listening on port 1212...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")

    while True:
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break

        decrypted_data = decrypt(encrypted_data)
        print(f"Decrypted data: {decrypted_data}")
        try:
            print(f"Received: {decrypted_data.decode('utf-8')}")
        except UnicodeDecodeError:
            print("Error: Decrypted data is not valid UTF-8.")

        response = input("Enter response: ")
        encrypted_response = encrypt(response.encode())
        conn.send(encrypted_response)

    conn.close()

if __name__ == "__main__":
    start_server()