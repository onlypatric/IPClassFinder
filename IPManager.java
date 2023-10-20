import java.util.Scanner;

/**
 * The {@code IPManager} class manages IP addresses and determines their classes.
 */
public class IPManager {
    private String ip;

    /**
     * Constructs an {@code IPManager} object and prompts the user for a valid IP
     * address.
     */
    public IPManager() {
        this.ip = getValidIp();
    }

    /**
     * Prompts the user for an IP address until a valid one is entered.
     *
     * @return The valid IP address entered by the user.
     */
    private String getValidIp() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Insert IP address: ");
            String ip = scanner.nextLine();
            if (ip.matches("^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$")) {
                scanner.close();
                return ip;
            } else {
                System.out.println("Invalid IP address");
            }
        }
    }

    /**
     * Determines the network class (A to E) of the IP address.
     *
     * @return The character representing the network class (A, B, C, D, E, or U for
     *         Unknown).
     */
    public char getNetClass() {
        String[] octets = ip.split("\\.");
        int firstOctet = Integer.parseInt(octets[0]);
        if (firstOctet >= 1 && firstOctet <= 126) {
            return 'A';
        } else if (firstOctet >= 128 && firstOctet <= 191) {
            return 'B';
        } else if (firstOctet >= 192 && firstOctet <= 223) {
            return 'C';
        } else if (firstOctet >= 224 && firstOctet <= 239) {
            return 'D';
        } else if (firstOctet >= 240 && firstOctet <= 255) {
            return 'E';
        } else {
            return 'U'; // U for Unknown
        }
    }

    /**
     * The main method creates an {@code IPManager} object and prints the network
     * class.
     *
     * @param args The command-line arguments (not used).
     */
    public static void main(String[] args) {
        IPManager ipManager = new IPManager();
        char netClass = ipManager.getNetClass();
        System.out.println("Network class: " + netClass);
    }
}
