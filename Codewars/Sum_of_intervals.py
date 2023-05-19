def sum_of_intervals(intervals):
    inter1 = 0
    inter2 = 0
    intervalo = 0
    for i in intervals:
        intervalo += i[-1] - i[0]
        
        saida += intervalo

    return saida




# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

if __name__ == "__main__":
    
    intervals = [(1, 5), (6, 10)]

    print(sum_of_intervals(intervals))