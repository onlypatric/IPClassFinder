import re

class IPManager:
    """Manages IP addresses determining their classes

    Returns:
        IPManager: IPManager object
    """
    def __init__(self):
        self.ip = self.get_valid_ip()

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

if __name__=="__main__":
    ip_manager = IPManager()
    netclass = ip_manager.get_netclass()

    print(f"Network class: {netclass}")