# Pretty print json data
import json

if __name__ == "__main__":
    samlpeJson = """{"key1": "value1", "key2": "value2", "key3": "value3" }"""
    ppjson = json.dumps(samlpeJson, indent=2, separators=(",", " = "))
    print(ppjson)
