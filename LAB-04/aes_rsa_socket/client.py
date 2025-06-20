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

try:
    print(f"Connecting to server on port {PORT}...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))
    print("Connected to server successfully!")
except ConnectionRefusedError:
    print(f"Could not connect to server on port {PORT}")
    print("Make sure the server is running and the port is correct")
    sys.exit(1)
except Exception as e:
    print(f"Error connecting to server: {e}")
    sys.exit(1)

try:
    client_key = RSA.generate(2048)
    print("Generated RSA key pair")
    
    print("Receiving server's public key...")
    server_public_key = RSA.import_key(client_socket.recv(2048))
    print("Received server's public key")
    
    print("Sending client's public key...")
    client_socket.send(client_key.publickey().export_key(format='PEM'))
    print("Sent client's public key")
    
    print("Receiving encrypted AES key...")
    encrypted_aes_key = client_socket.recv(2048)
    print("Received encrypted AES key")
    
    cipher_rsa = PKCS1_OAEP.new(client_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    print("Decrypted AES key successfully")
    
except Exception as e:
    print(f"Error during key exchange: {e}")
    client_socket.close()
    sys.exit(1)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key,encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key,AES.MODE_CBC,iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext),AES.block_size)
    return decrypted_message.decode()

# Add a flag to control the receive thread
running = True

def receive_messages():
    global running
    try:
        while running:
            try:
                encrypted_message = client_socket.recv(1024)
                if not encrypted_message:  # Connection closed by server
                    print("Server closed the connection")
                    break
                decrypted_message = decrypt_message(aes_key,encrypted_message)
                print("Received:", decrypted_message)
            except socket.error:
                if not running:
                    break
                raise
    except Exception as e:
        if running:  # Only print error if we're still supposed to be running
            print(f"Error receiving messages: {e}")
    finally:
        print("Stopping receive thread...")

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

try:
    while True:
        message = input("Enter message ('exit' to quit):")
        encrypted_message = encrypt_message(aes_key,message)
        client_socket.send(encrypted_message)
        if message.lower() == "exit":
            print("Closing connection...")
            break
except Exception as e:
    print(f"Error sending message: {e}")
finally:
    running = False  # Signal the receive thread to stop
    try:
        client_socket.shutdown(socket.SHUT_RDWR)
    except:
        pass
    client_socket.close()
    print("Connection closed")
    # Wait for receive thread to finish
    receive_thread.join(timeout=1.0)