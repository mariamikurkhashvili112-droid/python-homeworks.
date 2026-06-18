#1. შექმენით მთელი რიცხვების მინიმუმ 5 ელემენტიანი სია, გამოთვალეთ ყველა რიცხვის ჯამი
# და საშუალო, არ გამოიყენოთ ჩაშენებული ფუნქციები!

numbers_lst = [12, 25, 10, 3, 79, 45, 13]

total = 0
count = 0

for number in numbers_lst:
    total += number
    count += 1

average = total / count

print("Sum: ", total)
print("Average:", average)
#2. მოცემულია სია ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1], დაწერეთ ლოგიკა, როემლიც ამ ლისტში დატოვებს უნიკალურ
#ელემენტებს, ანუ არ განმეორდება ელემენტები. არ გამოიყენოთ set!

items = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]

unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print("Unique list:", unique)

#3. დააგენერირეთ 20 ელემენტიანი რიცხვების სია, რომელიც შევსებული იქნება -50 დან 50-მდე შემთხვევითი რიცხვებით და შექმენით მეორე
#სია, რომელიც პირველი სიიდან იქნება შევსებული მხოლოდ ლუწი რიცხვებით და დაბეჭდეთ ორივე სია, გამოიყენეთ აუცილებლად ლისტის გენერატორი!

import random

numbers = [random.randint(-50, 50) for i in range(20)]
even_numbers = [number for number in numbers if number % 2 == 0]

print("All numbers:", numbers)
print("Even numbers:", even_numbers)

#4. შექმენით ორი ლისტი long_names, short_names დაწერეთ პროგრამა რომელიც მომხმარებელს უსასრულოდ შეაყვანინებს სახელებს და შემოყვანილი სახელი თუ 3 სიმბოლოზე მეტი
#იქნება long_names სახელების ლისტში შეიტანს, ხოლო თუ ნაკლები იქნება short_names-ში. ლისტში უნდა ჩაიყაროს სახელები ისე, რომ პირველი ასოები იყოს დიდი,
#მაგალითად, მომხმარებელი თუ შემოიყვანს ასეთი სახით "daVit" ან "davit", ლისტში უნდა შეინახოთ "Davit" ასევე, თავსა და ბოლოში მოაშორეთ ცარიელი ადგილები!
#პროგრამა ჩერდება იმ შემთხვევაში, მომხმარებელი თუ შეიყვანს სიტყვას stop ან Stop ან exit ან Exit ან quit ან Quit

long_names = []
short_names = []

while True:
    name = input("Enter a name: ").strip().capitalize()

    if name == "Stop" or name == "Exit" or name == "Quit":
        break

    if len(name) > 3:
        long_names.append(name)
    else:
        short_names.append(name)

print("Long names:", long_names)
print("Short names:", short_names)