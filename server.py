import socket
import threading
import pygame
import math
import time
import colors
import sys
from threading import Thread
from target import *
from display import draw
from ultrasonicsensor import ultrasonicRead

# The range is set to 50 cm, to change it 
# change the range condition in the ultrasonicsensor module
# change the range condition in this module
# change scale in e and f in draw function in display module

print('Radar Start')

# initialize the program
x = pygame.init()

pygame.font.init()

defaultFont = pygame.font.get_default_font()

fontRenderer = pygame.font.Font(defaultFont, 20)

radarDisplay = pygame.display.set_mode((1400, 800))
    
pygame.display.set_caption('Radar Screen')

targets = {}
iAngle = -1
iDistance = -1

def radar_thread():
    global targets, iAngle, iDistance
    
    try:
        while True:

            # rotate from 0 to 180
            for angle in range(0, 180):
                distance = -1

                # change the condition if the range is changed
                if iDistance != -1 and iDistance <= 50 and iAngle == angle:
                    distance = iDistance
                    targets[angle] = Target(angle, distance)
                    print("yes")

                draw(radarDisplay, targets, angle, distance, fontRenderer)

                angle = 180 - angle

                time.sleep(0.01)


            # rotate from 180 to 0
            for angle in range(180, 0, -1):
                distance = -1

                # change the condition if the range is changed
                if iDistance != -1 and iDistance <= 50 and iAngle == angle:
                    distance = iDistance
                    targets[angle] = Target(angle, distance)
                    print("yes")

                draw(radarDisplay, targets, angle, distance, fontRenderer)

                angle = 180 - angle

                time.sleep(0.01)

            # detect if close is pressed to stop the program
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt

    except KeyboardInterrupt:
        print('Radar Exit')

    except Exception as e:
        print(e)
        print('Radar Exit')






# Define client_sockets as a global dictionary to handle multiple clients
client_sockets = {}

def handle_client(client_socket):
    global iAngle, iDistance
    while True:
        try:
            data_from_client = client_socket.recv(1024)
            if data_from_client:
                packet = data_from_client.decode()
                packets = packet.split("/")
                for p in packets:
                    if(p.startswith("angle:")):
                        iAngle = int(p.split(":")[1])
                        print(iAngle)
                    if(p.startswith("distance:")):
                        iDistance = int(p.split(":")[1])
                        print(iDistance)
                
        except:
            print("Error receiving data. Closing connection.")
            break

    client_socket.close()

def send_command(client_socket, command):
    try:
        client_socket.send(command.encode())
    except:
        print("Error sending command. Closing connection.")
        client_socket.close()
        del client_sockets[client_socket]

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = 'localhost'
    server_port = 8000
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print("Server listening on port 8000...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address[0]}:{client_address[1]}")

        client_sockets[client_socket] = client_address

        receive_thread = threading.Thread(target=handle_client, args=(client_socket,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_command, args=(client_socket, "Hello, client!"))
        send_thread.start()

# Start the radar thread
radar_thread = Thread(target=radar_thread, daemon=True)
radar_thread.start()

start_server()

# pygame.quit()
# sys.exit()