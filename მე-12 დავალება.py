#1 დავალება:
import csv

def save_users_info(n):
    users_data = []

    for i in range(n):
        print("Enter user details:")
        f_name = input("First name: ")
        l_name = input("Last name: ")

        while True:
            try:
                age = int(input("Age: "))
                break
            except ValueError:
                print("Please enter a number!")

        user_dict = {
            "ID": i + 1,
            "first_name": f_name,
            "last_name": l_name,
            "age": age
        }
        users_data.append(user_dict)

    headers = ["ID", "first_name", "last_name", "age"]
    with open("users.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(users_data)


save_users_info(3)

#2 დავალება :


import csv

passed_students = []
failed_students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        grade = int(row["Grade"])

        if grade < 50:
            failed_students.append(row)
        else:
            passed_students.append(row)

headers = ["ID", "First Name", "Last Name", "Grade"]

with open("failed_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(failed_students)

with open("passed_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(passed_students)

print(" DONE !  ")