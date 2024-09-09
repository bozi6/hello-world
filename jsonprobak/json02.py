# Parse the following JSON to get all the values of a key 'name' wihtin an array
import json

sampleJson = """[
    {
        "id":1,
        "name":"Béla",
        "color":[
            "red",
            "green"
        ]
    },
    {
        "id":2,
        "name":"Mari",
        "color":[
            "pink",
            "yellow"
        ]
    }
]"""

data = []


def main():
    """

    Parse the following JSON to get all the values of a key 'name' wihtin an array.

    :parameter: Null
    :return: Null

    """
    try:
        data = json.loads(sampleJson)
    except Exception as e:
        print(e)
    dataList = [item.get("name") for item in data]
    print(dataList)


if __name__ == "__main__":
    main()
