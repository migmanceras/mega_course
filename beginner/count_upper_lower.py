text = "This Sentence Has Mixed CASE Letters!"

uppercase = 0
lowercase = 0


for letter in text:
    if str.isalpha(letter):
        if str.islower(letter):
            lowercase = lowercase +1
        elif str.isupper(letter):
            uppercase = uppercase +1

print("The number of uppercase letters is: " + str(uppercase))
print("The number of lowercase letters is: " + str(lowercase))