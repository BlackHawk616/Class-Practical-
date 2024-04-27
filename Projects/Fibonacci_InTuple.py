# # Writing A Program To Print Fibonacci series and converting Into Tuple

t = int(input("How Many Terms You Want To Print :- "))

f1,f2 = 0,1

fs = []

# Converting Into List
for i in range(t):
    fs.append(f1)
    f1 , f2 = f2, f1 + f2

print(fs)
print(type(fs))

# Converting Into Tuple

ft = tuple(fs)

print(ft)
print(type(ft))