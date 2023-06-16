import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Traffic Redirection Script")
    parser.add_argument("--source-ip", help="Source IP address")
    parser.add_argument("--destination-ip", help="Destination IP address")
    args = parser.parse_args()

    source_ip = args.source_ip or input("Source IP address: ")
    destination_ip = args.destination_ip or input("Destination IP address: ")

    add_route(source_ip, destination_ip)
    add_route(destination_ip, source_ip)

    print("Traffic redirection configured successfully.")

def add_route(network, via):
    command = ["ip", "route", "add", network, "via", via]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
    print("Operation completed successfully.")
