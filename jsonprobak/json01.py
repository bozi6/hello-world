# Access the value of key2
import json

samlpeJson = """{"key1": "value1", "key2": "value2" }"""

data = json.loads(samlpeJson)
print(data['key2'])
