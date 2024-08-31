def fibonacci_test(num):

    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


num = int(input("digite um número: "))

if fibonacci_test(num):
    print("o número pertence à sequência de fibonacci.")
else:
    print("o número não pertence à sequência de fibonacci.")