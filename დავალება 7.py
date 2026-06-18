#1. მოცემულია სია:

#(სახელი, გვარი, ასაკი)

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

#დაწერეთ უსასრულო ციკლი, რომელშიც მომხმარებელს ჰკითხავთ სახელს, თუ სახელი იქნება მოცემულ სიაში, შემდეგ ჰკითხეთ გვარი და გვარიც თუ იქნება,
#დაბეჭდეთ მისი ასაკი, ხოლო თუ არ იქნება სახელი დაბეჭდეთ რომ არ არის მოცემული სახელი, შესაბამისად გვარი აღარ ჰკითხოთ, ანალოგიურად
#მოიქეცით გვარის კითხვის შემთხვევაშიც. ციკლი უნდა გაჩერდეს იმ შემთხვევაში თუ მომხმარებელი შემოიყვანს სიტყვას "stop".


while True:
    name = input("Enter name: ")

    if name == "stop":
        print("Program finished.")
        break

    name_exists = False
    for person in persons:
        if person[0] == name:
            name_exists = True
            break

    if name_exists == False:
        print("Name not found!")
        continue

    last_name = input("Enter last name: ")

    if last_name == "stop":
        print("Program finished.")
        break

    correct_person = False
    for person in persons:
        if person[0] == name and person[1] == last_name:
            print("Age is:", person[2])
            correct_person = True
            break

    if correct_person == False:
        print("Wrong last name!")

#2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
 #  იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
 #  დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)
 
###### W3School ში ვნახე union და symmetric difference და ვფიქრობ კარგად ერგება დავალების პირობებს,სლაიდებში არ იყო ნახსენები და კომენტარს ამიტომ ვაკეთებ.

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

set1 = set(word1)
set2 = set(word2)

same_letters = set1.intersection(set2)
different_letters = set1.symmetric_difference(set2)
all_letters = set1.union(set2)

print("Common characters:", same_letters)
print("Different characters:", different_letters)
print("All characters together:", all_letters)