# packages_compared.py
import paramiko
import csv
import json

# Constants
CONFIG_FILE = "config.json"
INPUT_CSV = "openwrt_packages.csv"
OUTPUT_ALL = "openwrt_packages_labeled.csv"
OUTPUT_ROM = "openwrt_packages_rom.csv"
OUTPUT_OVERLAY = "openwrt_packages_overlay.csv"


def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, "r") as config_file:
        return json.load(config_file)


def create_ssh_connection(host, port, username, password):
    """Establish an SSH connection."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, port=port)
    return ssh


def get_rom_packages(ssh_client):
    """Retrieve package names under the ROM directory."""
    command = "ls /rom/usr/lib/opkg/info/*.control"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    rom_control_files = stdout.read().decode().splitlines()
    stdout.channel.close()
    ssh_client.close()
    return {line.split('/')[-1].replace('.control', '') for line in rom_control_files}


def read_csv(file_path):
    """Read rows from a CSV file."""
    with open(file_path, newline="") as infile:
        return list(csv.DictReader(infile))


def write_csv(file_path, fieldnames, rows):
    """Write rows to a CSV file."""
    with open(file_path, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def categorize_packages(all_packages, rom_packages):
    """Categorize packages as 'rom' or 'overlay'."""
    categorized_rows = []
    rom_rows = []
    overlay_rows = []
    for row in all_packages:
        name = row["name"]
        pkg_type = "rom" if name in rom_packages else "overlay"
        row["type"] = pkg_type
        categorized_rows.append(row)
        (rom_rows if pkg_type == "rom" else overlay_rows).append(row)

    return categorized_rows, rom_rows, overlay_rows


def main():
    # Load configuration and establish SSH connection
    config = load_config(CONFIG_FILE)
    ssh = create_ssh_connection(
        config["host"], config.get("port", 22),
        config["username"], config["password"]
    )

    # Extract ROM package names
    rom_packages = get_rom_packages(ssh)

    # Read CSV data
    all_packages = read_csv(INPUT_CSV)
    fieldnames = all_packages[0].keys() | {"type"}

    # Categorize and write CSVs
    all_rows, rom_rows, overlay_rows = categorize_packages(all_packages, rom_packages)
    write_csv(OUTPUT_ALL, fieldnames, all_rows)
    write_csv(OUTPUT_ROM, fieldnames, rom_rows)
    write_csv(OUTPUT_OVERLAY, fieldnames, overlay_rows)

    # Export completion message
    print("✅ Exportok készen:")
    print(f"  • Teljes lista: {OUTPUT_ALL}")
    print(f"  • Alaptelepített (rom): {OUTPUT_ROM}")
    print(f"  • Külön telepített (overlay): {OUTPUT_OVERLAY}")


if __name__ == "__main__":
    main()
