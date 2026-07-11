import json

def add_new_persons(count):
    with open("persons.json", "r") as f:
        persons = json.load(f)

    if len(persons) > 0:
        last_id = persons[-1]["id"]
    else:
        last_id = 0

    for i in range(count):
        name = input("enter your name: ")
        age = int(input("enter your age: "))

        last_id += 1

        new_person = {
            "id": last_id,
            "name": name,
            "age": age
        }

        persons.append(new_person)

    with open("persons.json", "w") as f:
        json.dump(persons, f, indent=4)

