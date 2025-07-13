import paramiko
import csv
import json

# Constants
CONFIG_FILE = "config.json"
OUTPUT_CSV_FILE = "openwrt_packages.csv"


def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, "r") as config_file:
        return json.load(config_file)


def create_ssh_connection(host, port, username, password):
    """Establish an SSH connection safely."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password, port=port)
    return client


def retrieve_installed_packages(ssh_client):
    """Execute command to get installed packages and return parsed output."""
    command = "opkg list-installed"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    installed_packages = stdout.read().decode().splitlines()
    stdout.channel.close()
    return installed_packages


def process_packages(installed_packages):
    """Process package list into structured data (name, version)."""
    packages = []
    for package_line in installed_packages:
        parts = package_line.split(" - ")
        if len(parts) >= 2:
            name, version = parts[0], parts[1]
            packages.append((name, version))
    return packages


def write_packages_to_csv(file_path, packages):
    """Write package data to a CSV file."""
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "version"])
        writer.writerows(packages)


def main():
    """Main execution flow."""
    # Load configuration
    config = load_config(CONFIG_FILE)

    # Establish SSH connection
    with create_ssh_connection(
            config["host"], config.get("port", 22),
            config["username"], config["password"]
    ) as ssh_client:
        # Retrieve, process, and save package data
        installed_packages = retrieve_installed_packages(ssh_client)
        processed_packages = process_packages(installed_packages)
        write_packages_to_csv(OUTPUT_CSV_FILE, processed_packages)

    print(f"✅ CSV fájl elkészült: {OUTPUT_CSV_FILE} ({len(processed_packages)} csomag)")


if __name__ == "__main__":
    main()
