from puresnmp import get
from puresnmp.api.raw import get as raw_get

ip = "192.168.7.99"
community = "public"
oid = '1.3.6.1.2.1.3.1.1.3.0.1.192.168.7.99'  # only example

result = get(ip, community, oid)
raw_result = raw_get(ip, community, oid)

print(type(result), repr(result))
print(type(raw_result), repr(raw_result))
