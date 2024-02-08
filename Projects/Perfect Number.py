# Writing A Program To Check If the Given Number is perfect Number or not

n = int(input("Enter The Number Here :- "))

s = 0

for i in range(1,n):

    if (n%i == 0):

        s = s + i
if s == n:
    print("its a perfect Number")

else:
    print("Its not a perfect number")