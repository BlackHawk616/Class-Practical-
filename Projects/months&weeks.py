# Wrting A Program To Create A Dictionary When Key are weaks name

Week = {1:"Mon", 2:"Tue" ,3:"Wed",4:"Thu" ,5:"Fri" ,6:"Sat",7:"Sun"}

n = int(input("Enter The Week Number : - "))

if n in Week:
    print(Week[n])

else:
    print("Not Found In The Dict")
