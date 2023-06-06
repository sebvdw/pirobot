import socket

# Server information
server_address = 'localhost'  # Replace with the server IP address
server_port = 8000  # Replace with the server port number

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_address, server_port))
    print('Connected to the server.')

    while True:
        # Receive data from the server
        data = client_socket.recv(1024).decode()
        
        if not data:
            # No more data received, connection closed by the server
            print('Server disconnected.')
            break
        
        # Print the received command
        print('Received command:', data)
        
        # Process the command here (add your own code)
        # ...
        
except ConnectionRefusedError:
    print('Connection refused. Make sure the server is running.')
finally:
    # Close the client socket
    client_socket.close()
