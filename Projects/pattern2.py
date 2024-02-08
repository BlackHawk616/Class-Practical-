# Printing The Following Pattern

"""
1
12
123
1234
12345
"""

nr = 6

for i in range(1, nr+1):

    for j in range(1,i):
        print(j, end="")
    
    print()