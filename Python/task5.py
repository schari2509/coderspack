#Months

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = input("Enter month : ")
for i in range(12):
    if m == months[i]:
        print("No. of days : ", days[i])
        break
