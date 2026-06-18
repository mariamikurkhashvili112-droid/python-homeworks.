#1. დაწერეთ პროგრამა რომელიც მომხმარებელს ჰკითხავს წონას(კგ) და სიმაღლეს(მ), შეყვანილი მონაცემების
#საფუძველზე გამოითვლის BMI-ს(Body Mass Index). ფორმულა: წონა გაყოფილი სიმაღლის კვადრატზე
#თუ BMI ნაკლებია 19-ზე, გამოიტანეთ ინფო რომ ის არის underweight
#თუ BMI არის 19 და 25 შორის, გამოიტანეთ ინფო რომ ის არის normalweight
#თუ BMI მეტია 25-ზე, გამოიტანეთ ინფო რომ ის არის overweight

Height=float(input("Enter Your Height in cm: "))
Weight=float(input("Enter Your Weight in kg: "))

BMI=Weight/(Height**2)

if BMI < 19:
   print("underweight")
elif 19 <= BMI <= 25:
   print("normalweight")
else:
   print("overweight")

#2. #დაწერეთ კალკულატორის პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და არითმეტიკულ ოპერატორს,
#შესაბამისი ოპერატორის საფუძველზე გამოითვლის ამ ორი რიცხვის შედეგს.

Number1=float(input("Enter first number:"))
Number2=float(input("Enter second number:"))
Operator = input("Enter Operator (+,-,*,/,//,%,**):")

if Operator == "+":
    print(Number1+Number2)
elif Operator == "-":
    print(Number1-Number2)
elif Operator == "*":
    print(Number1*Number2)
elif Operator =="/":
    print(Number1/Number2)
elif Operator =="//":
    print(Number1+Number2)
elif Operator =="%":
    print(Number1%Number2)
elif Operator == "**":
    print(Number1**Number2)


#3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება 3 რიცხვს, ჯერ შეამოწმეთ ეს რიცხვები არ უდრიდეს ერთმანეთს,
#თუ რომელიმე ორი ერთმანეთს უდრის, დაპრინტეთ რომ შეიყვანოს განსხვავებული რიცხვები. თუ რიცხვები განსხვავებულია,
#იპოვეთ ყველაზე დიდი რიცხვი. არ გამოიყენოთ max ფუნქცია!

Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))
Number3 = float(input("Enter third number: "))

if Number1 == Number2 or Number1 == Number3 or Number2 == Number3:
    print("Please enter different numbers")
else:
    if Number1 > Number2 and Number1 > Number3:
        print(Number1)
    elif Number2 > Number1 and Number2 > Number3:
        print(Number2)
    else:
        print(Number3)