def increment_string(strng):
    tnum = ''
    count = 0
    neg_count = 0
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7','8','9']
    
    for i in strng:
        for j in numbers:
            if i == j:
                tnum += j
                count += 1
    num = int(tnum)
    
    if num == 0:
        num = 1
    elif num > 0:
        num += 1

    strng = strng.split(tnum)

    strng = strng[0] + str(num)
    
    
    
    return strng


# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python


if __name__ == "__main__":

    strng = ('foobar001')

    print(increment_string(strng))