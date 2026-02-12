# input :- a5k3b3 
# output :- afknbe

str = "a5k3b3"

res = "";

for i in range(0,len(str),2):
    sa= str[i]
    num = int(str[i+1])
    new = chr(ord(sa)+num)
    res +=sa+new
print(res)