from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity

nas_ip = '192.168.0.78'       # NAS IP címe
community = 'public'          # SNMP community string

# Lekérdezendő OID-ok
oids = {
    'sysDescr': '1.3.6.1.2.1.1.1.0',
    'sysName': '1.3.6.1.2.1.1.5.0'
}

# SNMP GET minden OID-ra
for label, oid in oids.items():
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((nas_ip, 161), timeout=1, retries=2),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(f"{label} → Hiba: {errorIndication}")
    elif errorStatus:
        print(f"{label} → Hiba: {errorStatus.prettyPrint()} at index {errorIndex}")
    else:
        for varBind in varBinds:
            print(f"{label} = {varBind[1]}")
