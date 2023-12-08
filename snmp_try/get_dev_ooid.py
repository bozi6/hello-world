"""
Get SNMP information

:return: prints finded smntp line
:rtype: str

"""
import asyncio


async def example():
    """
    Példa függvény a lekérésre

    :return: kimenet
    :rtype: str

    """
    client = PyWrapper(Client(ip, V2C(community)))
    output = await client.get(oid)
    return output


if __name__ == "__main__":
    from puresnmp import Client, V2C, PyWrapper

    ip = "192.168.7.99"
    community = "public"
    oid = "1.3.6.1.2.1.3.1.1.3.0.1.192.168.7.99"  # only example
    print(asyncio.run(example()))
