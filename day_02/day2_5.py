def print_binary(num):
    if num == 0:
        print(0)
        return

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    print(binary)
n = int(input("Enter a number: "))
print("Binary format:")
print_binary(n)
