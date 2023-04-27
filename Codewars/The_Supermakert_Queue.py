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

    customers = [6, 23, 38, 35, 10, 50, 33, 22, 29, 46, 37]
    n = 6

    # Deve retornar 76
    
    print(queue_time(customers, n))