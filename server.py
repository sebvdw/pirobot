import socket
import threading
import tkinter as tk

# Define client_socket as a global variable
client_socket = None

def handle_client():
    global client_socket  # Access the global client_socket variable

    while True:
        try:
            data = input("Enter data to send: ")
            client_socket.send(data.encode())
        except:
            print("Error sending data. Closing connection.")
            break

    client_socket.close()

def send_command(command):
    global client_socket  # Access the global client_socket variable
    client_socket.send(command.encode())

def create_window():
    window = tk.Tk()
    window.title("Command Window")

    forward_button = tk.Button(window, text="Forward", command=lambda: send_command("forward"))
    forward_button.pack()

    backward_button = tk.Button(window, text="Backward", command=lambda: send_command("backward"))
    backward_button.pack()

    right_button = tk.Button(window, text="Right", command=lambda: send_command("right"))
    right_button.pack()

    left_button = tk.Button(window, text="Left", command=lambda: send_command("left"))
    left_button.pack()

    window.mainloop()

def start_server():
    global client_socket  # Access the global client_socket variable

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = 'localhost'
    server_port = 8000
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print("Server listening on port 8000...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address[0]}:{client_address[1]}")
        client_thread = threading.Thread(target=handle_client)
        client_thread.start()

        # Create the tkinter window in the main thread (no need for a separate thread)
        create_window()

start_server()
