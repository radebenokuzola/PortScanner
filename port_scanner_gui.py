import socket
import threading
from tkinter import *
from tkinter import scrolledtext

# Function to scan a specific port
def scan_port(host, port, output_box):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            output_box.insert(END, f"Port {port} is open\n")
        sock.close()
    except Exception as e:
        output_box.insert(END, f"Error scanning port {port}: {e}\n")

# Function to perform the scan on multiple ports
def port_scanner(remote_host, output_box):
    try:
        remote_ip = socket.gethostbyname(remote_host)
        output_box.insert(END, f"Please wait, scanning remote host {remote_ip}\n")
        
        ports = [21, 22, 80, 443, 8080]  # Common ports to scan
        
        # Use threading to scan ports concurrently
        for port in ports:
            t = threading.Thread(target=scan_port, args=(remote_ip, port, output_box))
            t.start()

    except socket.gaierror:
        output_box.insert(END, "Hostname could not be resolved.\n")
    except Exception as e:
        output_box.insert(END, f"Error: {e}\n")

# GUI for the port scanner
def start_gui():
    window = Tk()
    window.title("Port Scanner")
    
    # Label for host entry
    lbl = Label(window, text="Enter remote host to scan:")
    lbl.grid(column=0, row=0, padx=10, pady=10)
    
    # Entry box for host input
    host_entry = Entry(window, width=30)
    host_entry.grid(column=1, row=0, padx=10, pady=10)
    
    # Scrolled text box to display output
    output_box = scrolledtext.ScrolledText(window, width=40, height=10)
    output_box.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    
    # Start scan button
    def start_scan():
        remote_host = host_entry.get()
        output_box.delete(1.0, END)  # Clear previous output
        port_scanner(remote_host, output_box)

    scan_button = Button(window, text="Start Scan", command=start_scan)
    scan_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    start_gui()
