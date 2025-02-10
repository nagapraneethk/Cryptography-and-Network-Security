import socket
from Crypto.Cipher import ARC4


KEYY = b'Praneethsecretkey'


def encrypt(file):
    with open(file, "rb") as filee:
        f_data = filee.read()
    cipher=ARC4.ARC4Cipher(KEYY)
    enc_data=cipher.encrypt(f_data)
    return enc_data


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1212))

    encrypted_message = encrypt("Text_input.txt")
    client_socket.send(encrypted_message)
    print("File sent to serverrr...")

    client_socket.close()

if __name__ == "__main__":
    start_client()