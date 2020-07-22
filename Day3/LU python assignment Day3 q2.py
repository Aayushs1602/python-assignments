number = int(input())

for i in range(2, (number//2) + 2):
    if number % i == 0:
        print("not a prime number")
        break
else:
    print("prime number")