"""
O laço While é utilizado quuando queremos repetir a eecuçao de um bloco
de código enquanto uma determinada condição é verdadeira.

Exemplos 
    - Execute uma leitra enquanto um valor não for atingido
    - Envio e-mails enquanto uma frase não for lida
"""
if __name__ == "__main__":

    i = 0

    while i < 10:
        print(i)
        i = i + 1
    
    # Assim como o laço for, podemos ter um comando break dentro do while
    # que vai encerra a execução desse loop imediatamente

    while i < 20:
        if i >15:
                break
        
        print(i)
        i += 1

    # Também podemos ter o comando continue dentro do while, que passa para a
    # próxima execução do loop

    while i < 40:

        if i % 2 == 0:
            print(f"O número {i} é par")
            i += 1
            continue
    
        print(i)
        i += 1