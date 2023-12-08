# Sort JSON keys and write into file
import json

if __name__ == "__main__":
    samlpeJson = {"id": 1, "name": "value2", "age": 29}

    print("Started writing JSON data into a file")
    with open("sampleJSON.json", "w") as write_file:
        json.dump(samlpeJson, write_file, indent=4, sort_keys=True)
    print("Done writing JSON data into a file")
