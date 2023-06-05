import socket

def run_client():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = 'localhost'  # Change this to your server's host
    server_port = 12345  # Change this to your server's port

    # Connect to the server
    client_socket.connect((server_host, server_port))
    print("Connected to {}:{}".format(server_host, server_port))

    # Send data to the server
    message = "Hello from the client!"
    client_socket.send(message.encode())

    # Receive the server's response
    response = client_socket.recv(1024).decode()
    print("Received response:", response)

    # Close the client socket
    client_socket.close()

if __name__ == '__main__':
    run_client()
