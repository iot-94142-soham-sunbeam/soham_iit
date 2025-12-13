num = int(input("Enter a 5-digit number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
