word = input("Enter a word/sentence\n")

vowelCount=0
consonantCount = 0
for letter in word.strip(" "):
    if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
        vowelCount += 1
    elif letter == " ":
        continue
    else:
        consonantCount += 1

print("No of vowels are :",vowelCount)
print("No of Consonants are :",consonantCount)
