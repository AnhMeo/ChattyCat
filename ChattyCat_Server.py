import socket
import threading

HOST = '0.0.0.0'
PORT = 9999

def handle_client(client_socket, address):
    print(f"[+] Connected to {address}")
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg.lower() == 'quit':
                print("[-] Client disconnected")
                break
            print(f"Client: {msg}")
            response = input("You: ")
            client_socket.send(response.encode('utf-8'))
        except:
            break
    client_socket.close()
