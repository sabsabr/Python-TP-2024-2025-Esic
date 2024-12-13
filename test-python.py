import socket
import matplotlib.pyplot as plt

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Définir un délai d'attente pour la connexion
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def visualize_ports(open_ports):
    plt.figure(figsize=(10, 5))
    plt.bar(open_ports, [1] * len(open_ports), tick_label=open_ports)
    plt.xlabel('Ports')
    plt.ylabel('Status')
    plt.title('Open Ports')
    plt.yticks([])
    plt.show()

def main():
    target_ip = input("Enter the target IP address: ")
    ports = list(range(1, 1025))  # Par exemple, scanner les ports de 1 à 1024
    open_ports = scan_ports(target_ip, ports)
    
    print(f"Open ports on {target_ip}: {open_ports}")
    visualize_ports(open_ports)

if __name__ == "__main__":
    main()