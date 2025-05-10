import socket
import threading

HOST = '0.0.0.0'
PORT = 9999

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"Server: {msg}")
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    threading.Thread(target = receive_messages, args = (client,), daemon = True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            client.send(msg.encode('utf-8'))
            break
        client.send(msg.encode('utf-8'))
    
    client.close()

if __name__ == "__main__":
    start_client()