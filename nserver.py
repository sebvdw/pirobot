import pygame
import socket
import threading
import time
from target import *
from display import draw

# Server configuration
HOST = '192.168.45.1'
PORT = 8000

# initialize the program
x = pygame.init()

pygame.font.init()

defaultFont = pygame.font.get_default_font()

fontRenderer = pygame.font.Font(defaultFont, 20)

radarDisplay = pygame.display.set_mode((1400, 800))
    
pygame.display.set_caption('Radar Screen')

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

targets = {}
iAngle = -1
iDistance = -1

def handle_client(client_socket, address):
    global iAngle, iDistance, targets, radarDisplay, fontRenderer
    # Handle individual client connections
    while True:
        packet = client_socket.recv(1024).decode()
        print(packet)
        if not packet:
            break
        if packet:
            packets = packet.split("/")
            for p in packets:
                if(p.startswith("angle:")):
                    a = int(p.split(":")[1][:2])
                if(p.startswith("distance:")):
                    d = int(p.split(":")[1][:2])
            drawRadar(a,d)  
                  

    # Close client socket
    client_socket.close()

def drawRadar(a,d):
    if d != -1 and d <= 50:
        targets[a] = Target(a, d)
    draw(radarDisplay, targets, a, d, fontRenderer)

def run_server():
    # Listen for client connections
    server_socket.listen(5)
    print('Server listening on {}:{}'.format(HOST, PORT))

    while True:
        # Accept new connections
        client_socket, address = server_socket.accept()
        print('Connected to', address)

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()


# Start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Main Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Cleanup
server_socket.close()
pygame.quit()
