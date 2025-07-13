"""
Get SNMP information
:return: Prints the retrieved SNMP line
:rtype: str
"""
import asyncio
from puresnmp import Client, V2C, PyWrapper

# Constants for SNMP configuration
SNMP_IP: str = "192.168.7.99"
SNMP_COMMUNITY: str = "public"
SNMP_OID: str = "1.3.6.1.2.1.3.1.1.3.0.1.192.168.7.99"  # Example OID


async def fetch_snmp_data() -> str:
    """
    Fetch SNMP data for the given configuration.
    :return: The SNMP data response
    :rtype: str
    """
    snmp_client = PyWrapper(Client(SNMP_IP, V2C(SNMP_COMMUNITY)))
    snmp_response = await snmp_client.get(SNMP_OID)
    return snmp_response


if __name__ == "__main__":
    print(asyncio.run(fetch_snmp_data()))
