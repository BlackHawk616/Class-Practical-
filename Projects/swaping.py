# Writing A Program To Input a List Of Number And Swap elemets at the even Location with the odd Location 

l1 = eval(input("Enter The List Here :- "))

l1 = list(l1)

print("Original List Is :", l1)

s = len(l1)

if s % 2 != 0:
    s = s - 1

for i in range(0,s,2):
    print(i, i+1)
    l1[i], l1[i+1] = l1[i+1], l1[i]

print("This Is The List After Swaping")

print(l1, "\nThis The List")
