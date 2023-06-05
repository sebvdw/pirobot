import socket
import threading

def handle_client(client_socket):
    # This function will handle individual client connections
    # Modify this function to implement your server's behavior
    # For example, you can receive data from the client and send a response

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print("Received data:", data)

        # Take input from the console
        user_input = input("Enter a command (forward, back, right, left): ")

        # Map the input to a response
        if user_input.lower() == "forward":
            response = "forward"
        elif user_input.lower() == "back":
            response = "back"
        elif user_input.lower() == "right":
            response = "right"
        elif user_input.lower() == "left":
            response = "left"
        else:
            response = "Invalid command"

        # Send the response back to the client
        client_socket.send(response.encode())

        # Close the client socket if the client sends an empty message
        if not data:
            client_socket.close()
            break

def run_server():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '192.168.45.1'  # Change this to your desired host
    server_port = 8000  # Change this to your desired port

    # Bind the server socket to a specific address and port
    server_socket.bind((server_host, server_port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print("Server listening on {}:{}".format(server_host, server_port))

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print("Client connected:", client_address)

        # Create a new thread for the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    run_server()
