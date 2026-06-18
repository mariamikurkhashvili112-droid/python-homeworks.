#1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#   [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით


pairs = [(1, 3), (4, 2), (2, 5)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)


#2. დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს,
#დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ
#შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)


def divide_numbers():
    try:
        a = int(input("Enter number1: "))
        b = int(input("Enter number2: "))
        return a / b
    except ValueError:
        print("Text not allowed")
    except ZeroDivisionError:
        print("Can not divide by zero")

print(divide_numbers())

#3. მოცემულია პროდუქტების ლისტი:

 #  products = [
#    {"name": "Laptop", "price": 1200},
 #   {"name": "Mouse", "price": 15},
#    {"name": "Keyboard", "price": 25},
 #   {"name": "Monitor", "price": 150},
 #   {"name": "Power", "price": 100},
#  {"name": "Pad", "price": 10},
#]

#filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
#map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
#sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
#reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი


from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

filtered_products = list(filter(lambda x: x["price"] < 100, products))
print(filtered_products)

mapped_products = list(map(lambda x: (x["name"], x["price"]), products))
print(mapped_products)

sorted_products = sorted(products, key=lambda x: x["price"])
print(sorted_products)

total_price = reduce(lambda a, b: a + b["price"], products, 0)
print(total_price)


#4. დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს

def recursive_sum(n):
    if n == 0 or n == 1:
        return n

    if n < 0:
        return "Sum is not defined for negative numbers!!!"

    return n + recursive_sum(n - 1)

print(recursive_sum(5))