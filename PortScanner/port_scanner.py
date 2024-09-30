import socket
import subprocess
import sys
from datetime import datetime

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a banner with information about which host we are scanning
print("-" * 60)
print(f"Please wait, scanning remote host {remoteServerIP}")
print("-" * 60)

# Check the time when the scan started
t1 = datetime.now()

# Using the range function to specify ports (1-1024)
# We also put in some error handling for catching errors
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("\nCouldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculate the difference in time to know how long the scan took
total = t2 - t1

# Printing the information to screen
print(f'Scanning Completed in: {total}')
