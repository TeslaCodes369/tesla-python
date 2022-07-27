from unittest import result


def IsPalindrome(s):
    print(s, end=' ')
    startIndex = 0
    endIndex = len(s)-1

    if endIndex == -1:
        return False
    elif endIndex < 2:
        return True

    result = True
    while startIndex < endIndex:
        if s[startIndex] != s[endIndex]:
            result = False
            break
        startIndex += 1
        endIndex -= 1

    return result


if __name__ == '__main__':
    print(IsPalindrome('hello'))
    print(IsPalindrome('asdsa'))
    print(IsPalindrome('aaaaaaaaaaaaaaaaaaa'))
    print(IsPalindrome(''))
