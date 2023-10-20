import ipaddress
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class IpParser:
    """
    Class for parsing IP addresses and calculating network properties.
    """
    def __init__(self, network, subnet) -> None:
        """
        Initializes the IpParser object with network and subnet information.
        
        Args:
            network (str): The network base address (IPv4 or IPv6).
            subnet (str): The network subnet mask (IPv4/IPv6/Integer).
        """
        self.network = network
        self.subnet = subnet
        self.network_address = ipaddress.ip_network(
            f'{network}/{subnet}', strict=False)
        self.broadcast_address = self.network_address.broadcast_address
        self.gateway_address = self.broadcast_address - 1
        self.dhcp_server_address = self.network_address.network_address + 1
        self.possible_dns_address = self.network_address.network_address + 2
        self.start_ip_address = self.network_address.network_address + 3
        self.num_users = self.network_address.num_addresses - 3
        # add something to determine if its A class, B class or C class the network
        first_octet = int(network.split('.')[0])
        if 1 <= first_octet <= 126:
            self.network_class = 'A'
        elif 128 <= first_octet <= 191:
            self.network_class = 'B'
        elif 192 <= first_octet <= 223:
            self.network_class = 'C'
        else:
            self.network_class = 'Unknown'
    @property
    def __dict__(self):
        """
        Generates a dictionary containing network properties.

        Returns:
            dict: A dictionary containing network properties.
        """
        return {
            'Network address': self.network_address.__str__(),
            'Broadcast': self.broadcast_address.__str__(),
            'Gateway': self.gateway_address.__str__(),
            'DHCP': self.dhcp_server_address.__str__(),
            'DNS': self.possible_dns_address.__str__(),
            'Start IP': self.start_ip_address.__str__(),
            "Network class":self.network_class,
            'Amount of possible users': str(self.num_users)
        }

class MainApp(QApplication):
    def __init__(self) -> None:
        """
        Initializes the MainApp object and sets up the GUI window.
        """
        super().__init__(sys.argv)
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle('Network generator')
        self.main_window.setMinimumSize(QSize(720,480))
        
        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(0)
        self.frame = QFrame()
        self.frame.setLayout(self.vbox)
        
        self.main_window.setCentralWidget(self.frame)
        
        self.titleSheet = "color:#fff;padding:0px;font-size:35px;font-weight:bold;margin:0px;"
        self.title2Sheet = "color:#fff;padding:0px;font-size:15px;font-weight:bold;margin:0px;"
        self.labels = [
            QLabel(f"Network generator"),
            QLabel(f"Network Base Address"),
            QLabel(f"Network Subnet mask"),
            QLabel(f"Result"),
        ]
        self.labels[0].setStyleSheet(self.titleSheet)
        self.labels[1].setStyleSheet(self.title2Sheet)
        self.labels[2].setStyleSheet(self.title2Sheet)
        self.labels[3].setStyleSheet(self.titleSheet)
        
        self.vbox.addWidget(self.labels[0])
        self.vbox.addWidget(self.labels[1])
        self.network_input = QLineEdit()
        self.network_input.setPlaceholderText("IPv4 or IPv6")
        self.vbox.addWidget(self.network_input)
        self.vbox.addWidget(self.labels[2])
        self.subnet_input = QLineEdit()
        self.subnet_input.setPlaceholderText("IPv4/IPv6/Integer")
        self.vbox.addWidget(self.subnet_input)
        
        self.submitBtn = QPushButton("Generate")
        self.vbox.addWidget(self.submitBtn)
        self.submitBtn.clicked.connect(self.generate)
        
        self.resultTable = QTableWidget()
        self.vbox.addWidget(self.labels[3])
        self.vbox.addWidget(self.resultTable)
        
        self.main_window.show()
    def generate(self):
        """
        Generates and displays network properties based on user input in a QTable.
        """
        network = self.network_input.text()
        subnet = self.subnet_input.text()
        parser = IpParser(network, subnet)
        dictionary = parser.__dict__
        self.resultTable.setRowCount(8)
        self.resultTable.setColumnCount(2)
        self.resultTable.setColumnWidth(0,300)
        self.resultTable.setColumnWidth(1,300)
        self.resultTable.setHorizontalHeaderLabels(['Property', 'Value'])
        index = 0
        for key, value in dictionary.items():
            self.resultTable.setItem(index,0,QTableWidgetItem(key))
            self.resultTable.setItem(index,1,QTableWidgetItem(str(value)))
            index+=1
app = MainApp()

app.exec()