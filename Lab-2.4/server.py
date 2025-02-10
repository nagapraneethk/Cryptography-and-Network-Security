import socket
from Crypto.Cipher import ARC4

KEYY = b'Praneethsecretkey'

def decrypt(enc_data):
    cipher = ARC4.ARC4Cipher(KEYY)
    dec_data=cipher.decrypt(enc_data)
    with open("decrypted_data.txt","wb") as f:
        f.write(dec_data)
    print("decrypted file saved as 'decrypted_data.txt'")
    print(f"decrypted data:\n{dec_data}")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1212))
    server_socket.listen(1)
    print("Server listening on port 1212...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")


    encrypted_data = conn.recv(1024)
    
    with open('encrypted_file.rc4', 'wb') as f:
        f.write(encrypted_data)
    print("Encrypted file saved as 'encrypted_file.rc4'.")

    decrypt(encrypted_data)

    conn.close()

if __name__ == "__main__":
    start_server()