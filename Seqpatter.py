# WAP  TO GENERATE THE SEQUENCE :-5,10,-15,20 UPTO n;


n = int(input("enter the total sequence"))

for i in range(1,n+1):
    term = i*5
    if i%2==1:
        term = -term
    print(term,end=" ")
