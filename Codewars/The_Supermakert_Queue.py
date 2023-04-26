def queue_time(customers, n):
    maior_tempo = 0
    total = 0

    for i in customers:
        if maior_tempo < i:
            maior_tempo = i
    
    if n == 1:
        return sum(customers)
    elif len(customers) <= n:
        return maior_tempo
    else:
        return sum(customers) / n



# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

if __name__ == "__main__":

    customers = [37, 8, 29, 31, 11, 47, 15, 8, 7, 37, 9, 25, 21, 9]
    n = 4

    # Deve retornar 76
    
    print(queue_time(customers, n))