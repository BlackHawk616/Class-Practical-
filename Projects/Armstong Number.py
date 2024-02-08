# Writing A Program To Check If The Given Number is armstong or not

n = int(input("Enter Here :- "))

s = 0

t = n

while t > 0:
    d = t % 10
   
    s += d ** 3

    t //= 10

if n == s:
    print("Its an armstong Number")

else:
    print("Its not an armstong Number")