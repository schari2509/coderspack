#Length of words

words = []
n = int(input("Enter the no. of words : "))
print("Enter the words : ")
for i in range(n):
    words.append(input())

length = len(words[0])

for i in range(1, n):
    if length < len(words[i]):
        length = len(words[i])

print("Length of longest word : ", length)
