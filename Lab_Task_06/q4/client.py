import socket,random
from Crypto.Cipher import ARC4

p = 23
g = 5

def get_private_key(p):
    return random.randint(2, p - 1)

def get_public_key(g, private_key, p):
    return pow(g, private_key, p)

def get_shared_secret(server_public_key, private_key, p):
    return pow(server_public_key, private_key, p)



def encrypted(input_data,shared_secret):
    cipher=ARC4.new(str(shared_secret).encode())
    enc_data=cipher.encrypt(input_data.encode())
    return enc_data


def decrypted(enc_data,shared_secret):
    cipher=ARC4.new(str(shared_secret).encode())
    dec_data=cipher.decrypt(enc_data)
    return dec_data.decode()



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1212))


client_private_key = get_private_key(p)
client_public_key = get_public_key(g, client_private_key, p)

client_socket.send(str(client_public_key).encode())

server_public_key = int(client_socket.recv(1024).decode())
shared_secret = get_shared_secret(server_public_key, client_private_key, p)


print("\n--- Key Exchange ---")
print(f"Prime (p): {p}, Base (g): {g}")
print(f"Client Private Key: {client_private_key}")
print(f"Client Public Key: {client_public_key}")
print(f"Server Public Key: {server_public_key}")
print(f"Shared Secret Key: {shared_secret}\n")
while True:
    message = input("Client: ")
    encrypted_message = encrypted(message, shared_secret)
    
    print("\n--- Message Sent ---")
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}\n")
    
    client_socket.send(encrypted_message)

    encrypted_message = client_socket.recv(1024)
    decrypted_message = decrypted(encrypted_message, shared_secret)
    
    print("\n--- Message Received ---")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}\n")


client_socket.close()





