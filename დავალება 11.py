# პირველი დავალება
counter = 1

with open("people.txt", "w") as file:
    while True:
        first_name = input("Enter your first name: ")
        if first_name.lower() == "stop":
            break
        last_name = input("Enter your last name: ")
        file.write(f"{counter}. {first_name} {last_name}\n")
        counter += 1

#მეორე დავალება

with open("persons.txt", "r") as file:
    lines = file.readlines()

under_50 = open("under_50.txt", "w")
over_50 = open("over_50.txt", "w")

for line in lines:
    line = line.strip()
    parts = line.split(", ")
    age = int(parts[1])
    if age < 50:
        under_50.write(line + "\n")
    else:
        over_50.write(line + "\n")

under_50.close()
over_50.close()