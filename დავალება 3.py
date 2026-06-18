#1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება რიცხვს და გამოითვლის ამ რიცხვის ფაქტორიალს, შეგახსენებთ რომ ფაქტორიალი
#არის ამ რიცხვის ნამრავლი ყველა მთელ რიცხვზე 1-მდე, ანუ 5-ის ფაქტორიალი არის 5 X 4 X 3 X 2 X 1 (დაწერეთ for ლუპის გამოყენებით)

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of", number, "is:", factorial)


#2. დაწერეთ გამრავლების ტაბულა ციკლების გამოყენებით, მაგალითად ასეთი სახით:
#1 * 1 = 1
#1 * 2 = 2
#1 * 3 = 3
#.........
#9 * 7 = 63
#9 * 8 = 72
#9 * 9 = 81


for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)


#3. ჩავთვალოთ რომ გვაქვს აპარატი, რომელშიც უნდა გადავიხადოთ რაღაც სერვისის გადასახადი, რომლის ღირებულებაც არის 50 ლარი,
#ხოლო აპარატი იღებს მხოლოდ 5, 10 და 20 ლარიან კუპიურებს და გვიბრუნებს ასევე ხურდას.

#დაწერეთ პროგრამა, რომელიც ბეჭდავს გადასახადი თანხის ოდენობას, შემდეგ მომხმარებელს სთხოვს მოათავსოს კუპიურა, თუ კუპიურა არ არის ვალიდური,
#დაბეჭდოს რომ შეიტანოს ვალიდური კუპიურა. თუ კუპიურა ვალიდურია, დაბეჭდოს რაც დარჩა გადასახდელი თანხა და კვლავ სთხოვოს მომხმარებელს კუპიურის
#მოთავსება, მანამ სანამ, გადასახდელი თანხა არ განულდება. ბოლოს კი დაუწეროს რამდენი ეკუთვნის ხურდა. ანუ ბოლო იტერაციაზე თუ დარჩენილია
#მაგალითად გადასახდელი თანხა 10 ლარი და მომხმარებელი შეიტანს 20 ლარიანს, დაუწეროს რომ ეკუთვნის 10 ლარი ხურდა.

SERVICE_COST = 50
VALID_BILLS = [5, 10, 20]

remaining = SERVICE_COST
print("Service fee:", SERVICE_COST, "GEL")

while remaining > 0:
    print("Amount left to pay:", remaining, "GEL")
    bill = int(input("Insert a bill: "))

    if bill not in VALID_BILLS:
        print("Invalid bill. Please insert a valid bill (5, 10 or 20 GEL).")
    else:
        remaining = remaining - bill
        if remaining < 0:
            change = remaining * -1
            print("Payment complete! Your change is:", change, "GEL")
        elif remaining == 0:
            print("Payment complete! No change.")
        else:
            print("Amount left to pay:", remaining, "GEL")



