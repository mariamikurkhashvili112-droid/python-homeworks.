#1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი,
#რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი


def commission_fee(func):
    def wrapper(balance, amount_to_pay):
        if balance < amount_to_pay + 1:
            return "Insufficient funds"

        balance -= 1
        return func(balance, amount_to_pay)

    return wrapper

@commission_fee
def transaction(balance, amount_to_pay):
    balance -= amount_to_pay
    return f"Transaction successful. Remaining balance: {balance}"

print(transaction(50, 20))
print(transaction(10, 20))
print(transaction(21, 20))


#2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#   შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს
#   ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#   და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!


class MethodCheckerMeta(type):
    def __new__(mcls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                if not attr_name.startswith('_'):
                    raise ValueError(f"Method '{attr_name}' is not valid. Must start with '_'")
        return super().__new__(mcls, name, bases, attrs)


class ValidClass(metaclass=MethodCheckerMeta):
    my_attribute = 100

    def __init__(self):
        self.another_attribute = 200

    def _test(self):
        return "This is a valid method"


valid_obj = ValidClass()
print(valid_obj._test())

try:
    class InvalidClass(metaclass=MethodCheckerMeta):
        my_attribute = 100

        def test(self):
            return "This will raise an error"
except ValueError as e:
    print(e)