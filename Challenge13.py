word = input("Enter a word: ")
vowels = "aeiou"
if word[0] in vowels:
    pig_latin = word + "way"
else:
    pig_latin = word[1:] + word[0] + "ay"

print(f"The word in Pig Latin is: {pig_latin}")