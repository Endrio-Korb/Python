def func(notas):
    notas.sort()
    return sum(notas[1:4]) / len(notas[1:4])

if __name__ == "__main__":
    print(f"{func([7,8,7,7,10]):.2f}")