import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            data = input("Enter data to send: ")
            client_socket.send(data.encode())
        except:
            print("Error sending data. Closing connection.")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.45.1', 8000))
    server_socket.listen(1)
    print("Server listening on port 8000...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address[0]}:{client_address[1]}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
