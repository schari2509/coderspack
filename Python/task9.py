#Odd Even

numbers = (45, 67, 22, 35, 80, 14, 26)

odd = 0
even = 0

for i in numbers:
    if i % 2 == 0:
        even  = even + 1
    else:
        odd = odd + 1

print("No. of odd numbers : ", odd)
print("No. of even numbers : ", even)
