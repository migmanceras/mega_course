text = "How many vowels and consonants are in this sentence?"

vowels = ['a','e','i','o','u']
count_vowels = 0
count_consonants = 0

for letter in text:
    if letter in vowels:
        count_vowels = count_vowels +1
    elif str.isalpha(letter):
        count_consonants = count_consonants +1

print("Vowels: " + str(count_vowels))
print("Consonants: " + str(count_consonants))