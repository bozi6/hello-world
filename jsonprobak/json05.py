# Access the nested key 'salary' from the following JSON
import json
samlpeJson = """{
    "company" : {
        "employee": {
            "name":"Emma",
            "payble":{
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}"""

data = json.loads(samlpeJson)
print("Salary from JSON")
print(data['company']['employee']['payble']['salary'])
