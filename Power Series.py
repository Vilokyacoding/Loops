2
n = int(input("Enter the number of terms: "))


i = 1

while i <= n:
    Power = i ** i
    if i == n:
        print(Power, end='')  
    else:
        print(Power, end=', ')
    i += 1
