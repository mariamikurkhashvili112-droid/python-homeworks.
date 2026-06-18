#1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას,
# პირველ სიტყვას და მეორე სიტყვას და შემოყვანილ წინადადებაში
#პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით.

text = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
result = text.replace(old_word, new_word)
print(result)


#2. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში იპოვის ყველაზე გრძელ სიტყვას და დაბეჭდავს მას. არ გამოიყენოთ max() ფუნქცია!

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)


#3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
#ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა, მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
#და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს, არ უნდა ჰქონდეს მნიშვნელობა.
#არ გამოიყენოთ sorted() ფუნქცია!

word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()
is_anagram = True

if len(word1) != len(word2):
    is_anagram = False
else:
    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            is_anagram = False

if is_anagram:
    print("They are anagrams!")
else:
    print("They are not anagrams.")