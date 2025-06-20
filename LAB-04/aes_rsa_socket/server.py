from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib
import sys

# Default port
PORT = 12345

# Allow custom port from command line
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print("Invalid port number. Using default port 12345")
    sys.exit(1)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Add socket reuse option
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind(('localhost', PORT))
    print(f"Server started on port {PORT}")
except OSError as e:
    print(f"Error binding to port {PORT}: {e}")
    print("Try using a different port number")
    sys.exit(1)

server_socket.listen(5)

server_key = RSA.generate(2048)

clients =[]

def encrypt_message(key,message):
    cipher = AES.new(key,AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(),AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext),AES.block_size)
    return decrypted_message.decode()

def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")
    
    try:
        client_socket.send(server_key.publickey().export_key(format='PEM'))
        
        client_received_key = RSA.import_key(client_socket.recv(2048))
        
        aes_key = get_random_bytes(16)
        
        cipher_rsa = PKCS1_OAEP.new(client_received_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        client_socket.send(encrypted_aes_key)
        
        clients.append((client_socket, aes_key))
        
        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:  # Client disconnected
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print(f"Received from {client_address}: {decrypted_message}")
            
            for client, key in clients:
                if client != client_socket:
                    try:
                        encrypted = encrypt_message(key, decrypted_message)
                        client.send(encrypted)
                    except Exception as e:
                        print(f"Error sending to client: {e}")
                        
            if decrypted_message.lower() == "exit":
                break
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        try:
            clients.remove((client_socket, aes_key))
        except ValueError:
            pass  # Client already removed
        client_socket.close()
        print(f"Connection with {client_address} closed")

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client,args=(client_socket, client_address))
    client_thread.start()
    
    