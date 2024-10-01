import socket
import threading

# Function to scan a single port
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Function to scan multiple ports using threading
def start_scan(host):
    ports = [21, 22, 80, 443, 8080]  # Common ports

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(host, port))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

if __name__ == "__main__":
    host = input("Enter a remote host to scan: ")
    start_scan(host)
