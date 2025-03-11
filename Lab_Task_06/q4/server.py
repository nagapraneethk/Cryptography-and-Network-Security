import socket,random
from Crypto.Cipher import ARC4

p = 23
g = 5

def get_private_key(p):
    return random.randint(2, p - 1)

def get_public_key(g, private_key, p):
    return pow(g, private_key, p)

def get_shared_secret(client_public_key, private_key, p):
    return pow(client_public_key, private_key, p)


def decrypted(enc_data,shared_secret):
    cipher=ARC4.new(str(shared_secret).encode())
    dec_data=cipher.decrypt(enc_data)
    return dec_data.decode()

def encrypted(input_data,shared_secret):
    cipher=ARC4.new(str(shared_secret).encode())
    enc_data=cipher.encrypt(input_data.encode())
    return enc_data



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1212))
server_socket.listen(1)
print("Server listening on port 1212...")

conn, addr = server_socket.accept()
print(f"Connection from {addr} established.")


server_private_key = get_private_key(p)
server_public_key = get_public_key(g, server_private_key, p)

conn.send(str(server_public_key).encode())
client_public_key = int(conn.recv(1024).decode())

shared_secret = get_shared_secret(client_public_key, server_private_key, p)


print("\n--- Key Exchange ---")
print(f"Prime (p): {p}, Base (g): {g}")
print(f"Server Private Key: {server_private_key}")
print(f"Server Public Key: {server_public_key}")
print(f"Client Public Key: {client_public_key}")
print(f"Shared Secret Key: {shared_secret}\n")


while True:
    encrypted_message = conn.recv(1024)
    decrypted_message = decrypted(encrypted_message, shared_secret)
    
    print("\n--- Message Received ---")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}\n")
    
    message = input("Server: ")
    encrypted_message = encrypted(message, shared_secret)
    
    print("\n--- Message Sent ---")
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}\n")
    
    conn.send(encrypted_message)

conn.close()



