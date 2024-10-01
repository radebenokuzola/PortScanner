# Port Scanner
A simple Python-based port scanner that allows users to scan common ports on a remote host and displays the results in a graphical interface (GUI) using Tkinter.

## Installation
To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/radebenokuzola/PortScanner.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd PortScanner
   ```

3. **Run the Python script**:
   ```bash
   python port_scanner.py
   ```

Make sure you have Python installed on your system. You can download it from [Python.org](https://www.python.org/).


## Usage
- Open the `port_scanner.py` program.
- Enter the remote host (e.g., google.com).
- Press "Start Scan" to scan common ports (21, 22, 80, 443, 8080).
- The scan results will be displayed in the text box below.

## Features
- GUI built with Tkinter for user-friendly interaction.
- Scans for open ports on a given remote host.
- Multi-threaded port scanning for faster results.

## Future Improvements
- Support for custom port ranges.
- Add a progress bar for long scans.
- Enhanced error handling for unreachable hosts.
