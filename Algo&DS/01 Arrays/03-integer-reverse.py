def reverseInt(num):
    print(num, end=' -> ')
    reverseNum = 0

    while num > 0:
        rem = num % 10
        reverseNum = reverseNum * 10 + rem
        num = num//10

    return reverseNum


if __name__ == '__main__':
    print(reverseInt(345))
    print(reverseInt(3234234212345))
    print(reverseInt(343335))
    print(reverseInt(345000))
    print(reverseInt(1234))
    print(reverseInt(0))
