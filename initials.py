name = str(input("Name: ")).title()

for n in name:
    if n.isupper():
        print(n, end=" ")
