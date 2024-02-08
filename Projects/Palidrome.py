n = int(input("Enter Here :- "))

wn = n

r = 0

while wn > 0:
    d = wn % 10
    
    r = r * 10 + d

    wn = wn //10

if n == r :
    print("Its an palidrom number")

else:
    print("its not a palidrome number")