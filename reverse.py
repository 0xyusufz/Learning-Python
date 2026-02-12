str = input("enter the string: ")

new_str = str.split()
res = []

for i in new_str:
    res.append(i[::-1])

result = " ".join(res)
print(result)