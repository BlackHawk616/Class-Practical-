# Writing A Program To input a tuple/list of element an search a given number in list/tuple

tl = eval(input("Enter The Tuple/list Element Here :- "))

print(tl)

print("Enter The Element Want To Seach In List/Tuple")

el = int(input("Enter Here (Only Numbers) : - "))

for i in tl :
    if el == i:
        print("The Item is found In the list")

    else:
        print("Not Found")
        break

