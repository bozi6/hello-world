import asyncio
import csv
from puresnmp import Client, V2C, PyWrapper

# Constants
IP_ADDRESS = "192.168.0.78"
COMMUNITY_STRING = "public"
OUTPUT_CSV_FILE = "nas_snmp_output.csv"

# OIDs to fetch
OIDS = {
    'sysDescr' : '1.3.6.1.2.1.1.1.0',
    'sysUpTime': '1.3.6.1.2.1.1.3.0',
    'sysName'  : '1.3.6.1.2.1.1.5.0',
    'HDD1_temp': '1.3.6.1.4.1.6574.2.1.1.6.1',
    'HDD2_temp': '1.3.6.1.4.1.6574.2.1.1.6.2'
}


async def fetch_snmp_data(snmp_client: PyWrapper, oids: dict) -> list[tuple[str, str, str]]:
    """Fetch SNMP data for given OIDs and display in the console."""
    results = []
    print("\nSNMP Query Results:\n-------------------")
    for label, oid in oids.items():
        try:
            value = await snmp_client.get(oid)
            result = (label, oid, str(value))
        except Exception as e:
            result = (label, oid, f"ERROR: {e}")
        results.append(result)
        print(f"Label: {result[0]}, OID: {result[1]}, Value: {result[2]}")
    print("-------------------")
    return results


def save_to_csv(file_path: str, data: list[tuple[str, str, str]]) -> None:
    """Save the SNMP data to a CSV file."""
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Label", "OID", "Value"])
        writer.writerows(data)
    print(f"✅ Data saved to: {file_path}")


async def main() -> None:
    """Main SNMP querying function."""
    snmp_client = PyWrapper(Client(IP_ADDRESS, V2C(COMMUNITY_STRING)))
    snmp_results = await fetch_snmp_data(snmp_client, OIDS)
    save_to_csv(OUTPUT_CSV_FILE, snmp_results)


if __name__ == "__main__":
    asyncio.run(main())
