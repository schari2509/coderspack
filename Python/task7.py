#Median

values = []
print("Enter 3 values: ")
for i in range(3):
    values.append(input())

values.sort()
print("Median : ", values[1])
    
