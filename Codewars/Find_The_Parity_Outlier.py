def find_outlier(integers):
    odd = []
    even = []

    for i in integers:
        if (i % 2) == 0:
            even.append(i)
        elif (i % 2) != 0:
            odd.append(i)
    
    if len(odd) == 1:
        return odd[0]
    elif len(even) == 1:
        return even[0]


# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python


if __name__ == "__main__":

    integers = [2, 4, 6, 8, 10, 3]

    print(find_outlier(integers))