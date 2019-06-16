#Product of a list

numbers = [8, 2, 3, -1, 7]

def multiply():
    product = 1
    for i in numbers:
        product = product * i

    print("Product : ", product)

multiply()
