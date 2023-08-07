import socket
import ssl
import nmap

def check_ssl_certificate(hostname, port):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(f"SSL certificate for {hostname}:{port} is valid.")
    except ssl.SSLError:
        print(f"SSL certificate for {hostname}:{port} is invalid or expired.")
    except ConnectionRefusedError:
        print(f"Connection refused to {hostname}:{port}. The service may not be running.")
    except socket.timeout:
        print(f"Connection to {hostname}:{port} timed out.")

def check_open_ports(hostname, ports):
    for port in ports:
        try:
            with socket.create_connection((hostname, port), timeout=5):
                print(f"Port {port} is open on {hostname}.")
        except ConnectionRefusedError:
            print(f"Port {port} is closed on {hostname}.")
        except socket.timeout:
            print(f"Connection to port {port} on {hostname} timed out.")

def scan_for_vulnerabilities(hostname):
    scanner = nmap.PortScanner()
    scan_result = scanner.scan(hostname, arguments='-T4 -F')
    print(f"Scanning {hostname} for potential vulnerabilities...")
    for port, result in scan_result['scan'][hostname]['tcp'].items():
        if result['state'] == 'open':
            print(f"Port {port} ({result['name']}): {result['product']} - {result['version']}")

def main():
    hostname = '194.195.116.6'
    ports_to_check = [80, 443, 22, 3306]  # Add more ports as needed

    check_ssl_certificate(hostname, 443)
    check_open_ports(hostname, ports_to_check)
    scan_for_vulnerabilities(hostname)

if __name__ == "__main__":
    main()
