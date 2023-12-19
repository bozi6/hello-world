# Access the value of key2
import json

jsondata = """{"key1": "value1", "key2": "value2" }"""


def jload(jsoncuc):
    """
    Prints the getted json stuff

    :param jsoncuc: json
    :type jsoncuc: str
    :return: data["key2"] value
    :rtype: dict elem
    """
    data = json.loads(jsoncuc)
    print(data["key2"])


if __name__ == "__main__":
    jload(jsondata)
