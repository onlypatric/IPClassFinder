# Network Generator Application

## Description

The **Network Generator Application** is a Python program that allows users to generate and analyze network configurations based on given IP addresses and subnet masks. It provides a graphical user interface (GUI) version and a command-line interface (CLI) version.

## Features

- **GUI Version:**
  - User-friendly interface to input IP addresses and subnet masks.
  - Calculates network properties such as network address, broadcast address, gateway address, DHCP server address, DNS server address, start IP address, network class, and the number of possible users.
  - Displays the results in a table format.
  - Supports both IPv4 and IPv6 addresses.

- **CLI Version:**
  - Command-line interface to input IP addresses.
  - Determines the network class (A to E) of the given IP address.
  - Provides clear and concise output indicating the network class.

## Installation and Usage

1. **GUI Version:**
   - Required Dependencies: PyQt6
   - Installation: `pip install PyQt6`
   - Installation: `pip install ipaddress`
   - Run the application: Execute the provided GUI script.
   - Enter the IP address and subnet mask, click "Generate," and view the results.

2. **CLI Version:**
   - No additional dependencies required.
   - Run the application: Execute the provided CLI script.
   - Enter the IP address when prompted and view the network class output.

## GUI Version Usage Example

1. Launch the application.
2. Input the network base address (IPv4 or IPv6) and the network subnet mask.
3. Click "Generate."
4. View the calculated network properties in the result table.

## CLI Version Usage Example

1. Run the CLI script in a terminal or command prompt.
2. Enter the IP address when prompted.
3. View the output displaying the network class (A to E) of the given IP address.

### Repository Structure

- **`GUI.py`**: Contains the code for the GUI version of the Network Generator Application.
- **`CLI.py`**: Contains the code for the CLI version of the Network Generator Application.
- **`IPManager.java`**: Contains the code for the Java CLI version of the Network Generator Application.
- **`README.md`**: Documentation file providing information about the application and its usage.

## Author

- Pintescul Patric
- Chirdo Pietro

---

Feel free to customize the README with your name, license information, and any other details specific to your project.
