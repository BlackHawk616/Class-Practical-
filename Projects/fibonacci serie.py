# Writing A Program To Print Fibonacci series

t = int(input("Enter How Many Terms You Want To Print ? :- "))

f = 0
f2 = 1

for i in range(2,t):

    n = f + f2
    print(f, end=',')
    f = f2
    f2 = n
