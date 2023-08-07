import requests
import socket
import ssl

def check_ssl_certificate(hostname, port=443):
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

def check_website_security(url):
    # Check SSL certificate
    if url.startswith("https://"):
        check_ssl_certificate(url.split("://")[1])

    # Check open ports
    hostname = url.split("://")[-1].split("/")[0]
    ports_to_check = [80, 443, 22, 3306]  # Add more ports as needed
    check_open_ports(hostname, ports_to_check)

    # Check website availability
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Website at {url} is reachable.")
        else:
            print(f"Error: Website at {url} returned status code {response.status_code}.")
    except requests.RequestException:
        print(f"Error: Website at {url} is not reachable.")

def main():
    website_url = 'http://training.host4india.in/durgesh2/'
    check_website_security(website_url)

if __name__ == "__main__":
    main()
