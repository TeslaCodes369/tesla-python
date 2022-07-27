def IsAnagram(str1, str2):
    print(str1, str2, end=' -> ')

    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return False

    if (sorted(str1) == sorted(str2)):
        return True

    return False


def IsAnagramV2(str1, str2):
    print(str1, str2, end=' -> ')

    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return False

    charDic = {}
    for ch in str1:
        if ch in charDic:
            charDic[ch] += 1
        else:
            charDic[ch] = 1

    for ch in str2:
        if ch in charDic:
            if charDic[ch] == 0:
                return False
            else:
                charDic[ch] -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    print(IsAnagram('hello', 'iaddo'))
    print(IsAnagram('hello', 'lhelo'))
    print(IsAnagram('hello12', '12lhelo'))
    print(IsAnagramV2('hello', 'iaddo'))
    print(IsAnagramV2('hello', 'lhelo'))
    print(IsAnagramV2('hello12', '12lhelo'))
