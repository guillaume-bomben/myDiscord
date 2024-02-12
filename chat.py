import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            break

def start_chat_client():
    username = input("Enter your username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.send(username.encode('utf-8'))

    welcome_message = client_socket.recv(1024).decode('utf-8')
    print(welcome_message)

    message_receiver = threading.Thread(target=receive_messages, args=(client_socket,))
    message_receiver.start()

    while True:
        message = input()
        client_socket.send(f"{username}: {message}".encode('utf-8'))

if __name__ == "__main__":
    start_chat_client()

