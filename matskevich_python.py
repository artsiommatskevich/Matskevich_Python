try:
    number = int(input("Make a numeric input: "))

    if number > 7:
        print("Hello")
except ValueError:
    pass

name = input("Please, input a name: ")
if name == "John":
    print(f'Hello, {name}')
elif name != "John":
    print("There is no such name")

array = input("Please, enter a numeric array: ")

for n in array:
    try:
        if (int(n) % 3) == 0:
            print(n, end ='')
    except ValueError:
        pass
print()

