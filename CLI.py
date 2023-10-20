import re

class IPManager:
    """Manages IP addresses determining their classes and network/host parts

    Returns:
        IPManager: IPManager object
    """
    def __init__(self):
        self.ip = self.get_valid_ip()
        self.subnet_mask = {"A":"255.0.0.0","B":"255.255.0.0","C":"255.255.255.0","D":"0.0.0.0","E":"0.0.0.0","Unknown":"255.255.255.255"}[self.get_netclass()]

    def get_valid_ip(self):
        """Finds valid ip and returns it, checking with regexp

        Returns:
            str: checked ip address
        """
        while True:
            ip = input("Insert IP address: ")
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
                return ip
            else:
                print("Invalid IP address")

    def get_subnet_mask(self):
        """Finds valid subnet mask or offset and returns it, checking with regexp

        Returns:
            str: checked subnet mask or offset
        """
        while True:
            mask = input("Insert Subnet Mask or Offset: ")
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", mask):
                return mask
            else:
                print("Invalid Subnet Mask or Offset")

    def get_netclass(self):
        """Find the network class of the ip address

        Returns:
            str: char containing the netclass (from A to E, else unknown to avoid errors)
        """
        octt = int(self.ip.split('.')[0])
        if 1 <= octt <= 126:
            netclass = 'A'
        elif 128 <= octt <= 191:
            netclass = 'B'
        elif 192 <= octt <= 223:
            netclass = 'C'
        elif 224 <= octt <= 239:
            netclass = 'D'
        elif 240 <= octt <= 255:
            netclass = 'E'
        else:
            netclass = 'Unknown'
        
        return netclass

    def get_network_host_parts(self):
        """Splits IP address into network and host parts based on subnet mask or offset

        Returns:
            tuple: (network_part, host_part)
        """
        ip_parts = list(map(int, self.ip.split('.')))
        
        network_part = '.'.join(str(ip_parts[i]) for i in range(
            *{"A":(0,1),"B":(0,2),"C":(0,3),"D":(0,),"E":(0,),"Unknown":(4,)}[self.get_netclass()]
            ))
        host_part = '.'.join(str(ip_parts[i]) for i in range(
            *{"A":(1,4),"B":(2,4),"C":(3,4),"D":(4,),"E":(4,),"Unknown":(0,)}[self.get_netclass()]
            ))

        return network_part, host_part

if __name__ == "__main__":
    ip_manager = IPManager()
    netclass = ip_manager.get_netclass()
    network_part, host_part = ip_manager.get_network_host_parts()

    # ANSI escape codes for colored output
    GREEN = '\033[92m'
    RESET = '\033[0m'

    BLUE = '\033[94m'
    print(f"Network class: {netclass}")
    print(f"Net subnet configuration: {GREEN}{network_part}{RESET}{'.' if network_part!='' else ''}{BLUE}{host_part}{RESET}")
