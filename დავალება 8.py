
#1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, მომხმარებელმა თუ შეიყვანა ტექსტი Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ასოა ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.

import math

def text_info(text):
    count = sum(1 for char in text if char.isupper())
    upper_text = text.upper()
    return count, upper_text

text = input("Please enter a text: ")
count, upper_text = text_info(text)

print(count)
print(upper_text)

#2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
 #  firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
 #  last_name და ასე შემდეგ.


import math

def camel_to_snake(text):
    result = ""
    for letter in text:
        if letter.isupper() and result != "":
            result += "_" + letter.lower()
        else:
            result += letter.lower()
    return result

text = input("Please enter a camel case variable: ")
print(camel_to_snake(text))