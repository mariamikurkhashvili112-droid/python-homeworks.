#1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#   ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის
#   შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი

def sum_numbers(times=5):
    inputs = []
    count = 0

    while count < times:
        num = input("Please enter a number: ")
        inputs.append(int(num))
        count = count + 1

    return sum(inputs)

print(sum_numbers())


#2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#   ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

def separate_numbers(*args):
    odd_list = []
    even_list = []

    for num in args:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return odd_list, even_list

print(separate_numbers(3, 5, 4, 34, 43, 66, 57, 98, 129, 1450))

#3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#   და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#  შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#   ჰქონდეს მნიშვნელობა!)


def count_words(sentence):
    clean_sentence = sentence.lower().replace(".", "")
    words = clean_sentence.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count

user_text = input("Enter a sentence: ")

print(count_words(user_text))