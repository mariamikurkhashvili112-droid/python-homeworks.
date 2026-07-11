#გვაქვს შემდეგი კლასი და ინსტანსი:

#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def __str__(self):
#        return f"Person: ({self.name}, {self.age})"

#p1 = Person("Otar", 35)

#დაწერეთ სერიალაიზერ ფუნქცია, რომელიც დაგეხმარებათ არსებული კლასის ობიექტი გადააქციოთ ისეთ ობიექტად,
#რომ შემდეგ ტექსტურ ფაილში ჩაწეროთ შემდეგი სტრუქტურით:
#Name: Otar, Age: 35
#რათქმაუნდა ჩაწერეთ ფაილში.
#არსებული ფაილიდან წაიკითხეთ ინფორმაცია.
#ასევე დაწერეთ დესერიალაიზერ ფუნქცია, რომელიც ზემოაღნიშნული სტრუქტურის ფაილიდან წაკითხულ ინფორმაციას აქცევს ისევ
#Person კლასის ობიექტად.(ჩათვალეთ რომ მხოლოდ ერთ ხაზს წერთ ფაილში და წაკითხვითაც ერთ ხაზს კითხულობთ)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

p1 = Person("Nino", 25)

def person_serializer(obj):
    if isinstance(obj, Person):
        return f"Name: {obj.name}, Age: {obj.age}"
    return "Object is not of type Person"

serialized_person = person_serializer(p1)

with open("person_data.txt", "w") as file:
    file.write(serialized_person)

with open("person_data.txt", "r") as file:
    file_data = file.read()

def person_deserializer(data_string):
    parts = data_string.split(", ")

    name = parts[0].split(": ")[1]

    age = int(parts[1].split(": ")[1])

    return Person(name, age)

new_person = person_deserializer(file_data)

print(new_person)