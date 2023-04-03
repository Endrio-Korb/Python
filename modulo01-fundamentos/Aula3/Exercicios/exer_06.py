def calcula_media(lista_nota):
    lista_nota.sort()
    lista_nota = lista_nota[1:4]
    return sum(lista_nota) / len(lista_nota)

def status(calcula_media):
    if calcula_media < 6:
        print(f"Reprovado.")
    elif calcula_media < 8:
        print(f"Em exame.")
    else:
        print(f"Aprovado.")

if __name__ == "__main__":
    
    lista_nota = []
    contador = 0
    nota = 0
    while contador < 5:
        nota = (int(input("Informe a nota do aluno: ")))
        if nota >= 0 and nota <= 10:
            lista_nota.append(nota)
            contador += 1
        else:
            print("Nota invalida insira uma nota válida.")
    
    print(f"A media do aluno é de : {calcula_media(lista_nota):.2f}")
    status(calcula_media(lista_nota))
