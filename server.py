import socket

def handle_client(client_socket):
    # This function will handle individual client connections
    # Modify this function to implement your server's behavior
    # For example, you can receive data from the client and send a response

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print("Received data:", data)

    # Send a response back to the client
    response = "Hello from the server!"
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()

def run_server():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = 'localhost'  # Change this to your desired host
    server_port = 12345  # Change this to your desired port

    # Bind the server socket to a specific address and port
    server_socket.bind((server_host, server_port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print("Server listening on {}:{}".format(server_host, server_port))

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print("Client connected:", client_address)

        # Handle the client connection in a separate thread or process
        handle_client(client_socket)

if __name__ == '__main__':
    run_server()
