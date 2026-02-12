str = input("enter the string").lower()
vowel = "aeiou"
for v in vowel:
    print(v,"=",str.count(v))