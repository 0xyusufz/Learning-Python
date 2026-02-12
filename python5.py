str = input("entr the srring").lower()
vowel = "aeiou"
found = set()

for ch in str:
    if ch in  vowel:
        found.add(ch)
print(found)