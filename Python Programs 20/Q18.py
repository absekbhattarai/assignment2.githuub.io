import json

print("Dictionaries: ")
person = {"name": "Absek", "age": 20}
print(person)
print("Converting to JSON: \n")
person_dict = json.dumps(person, indent = 2)
print( person_dict)

print("Now, converting into dictionaries from JSON\n")
json_string = json.loads(person_dict)
print(json_string)


